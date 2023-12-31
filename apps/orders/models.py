from django.db import models
from uuid import uuid4
from apps.core.models import AbstractBaseModel
from apps.users.models import Customer
from apps.core.constants import PAYMENT_STATUS_CHOICES, ORDER_STATUS
from apps.restaurants.models import Restaurant, MenuItem
# Create your models here.
class Order(AbstractBaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, default="pending")
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default="processing")
    order_items = models.JSONField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)
    


class OrderItem(AbstractBaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT, related_name="orderitems")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.menu_item.name
    
