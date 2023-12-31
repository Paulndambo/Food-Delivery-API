from django.db import transaction
from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.restaurants.models import MenuItem
from apps.users.models import Customer

class OrderSerializer(serializers.ModelSerializer):
    ordered_items = serializers.SerializerMethodField()
    order_cost = serializers.SerializerMethodField()
    customer_details = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = { 
            "customer": {"write_only": True, },  
            "restaurant": {"write_only": True, },
            "order_items": {"write_only": True, },
        }

    def get_restaurant_name(self, obj):
        if obj.restaurant:
            return obj.restaurant.name
        else:
            return None


    def get_ordered_items(self, obj):
        return obj.items.values('menu_item__name', 'quantity', 'unit_price')
    
    def get_order_cost(self, obj):
        return sum(obj.items.values_list("unit_price", flat=True))
    
    def get_customer_details(self, obj):
        user = obj.customer.user
        customer = obj.customer
        customer_object = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "username": user.username,
            "role": user.role,
            "phone_number": customer.phone_number,
            "gender": customer.gender,
            "location": customer.location,
            "city": customer.city,
            "country": customer.country
        }
        return customer_object
    

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["user"]
        customer = Customer.objects.filter(user=user).first()
        if not customer:
            customer = Customer.objects.create(user=user)
        
        try:
            order_items = validated_data["order_items"]
            customer = customer #validated_data["customer"]
            restaurant = validated_data.get("restaurant")
            order = Order.objects.create(customer=customer, restaurant=restaurant)
            order_item_objects = []
            for item in order_items:
                m_item = MenuItem.objects.get(id=item["menu_item"])
                order_item_objects.append(
                    OrderItem(
                        order=order,
                        menu_item= m_item,
                        quantity=item["quantity"],
                        unit_price = m_item.price * item["quantity"] - (m_item.discount/100 * m_item.price)
                    )
                )
            OrderItem.objects.bulk_create(order_item_objects)
            return order
        except Exception as e:
            raise e
        
