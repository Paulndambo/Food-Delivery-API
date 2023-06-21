from django.db import transaction
from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.restaurants.models import MenuItem

class OrderSerializer(serializers.ModelSerializer):
    ordered_items = serializers.SerializerMethodField()
    order_cost = serializers.SerializerMethodField()
    customer_details = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = { "customer": {"write_only": True, },  "order_items": {"write_only": True, },}


    def get_ordered_items(self, obj):
        return obj.items.values()
    
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
        try:
            order_items = validated_data["order_items"]
            customer = validated_data["customer"]
            restaurant = validated_data["restaurant"]
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
        
