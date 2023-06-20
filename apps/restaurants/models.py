from django.db import models
from apps.core.models import AbstractBaseModel
from django.conf import settings
from apps.core.constants import TABLE_STATUS_CHOICES

# Create your models here.
class Restaurant(AbstractBaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.JSONField(null=True)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RestaurantTable(AbstractBaseModel):
    table_number = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=1)
    status = models.CharField(max_length=255, choices=TABLE_STATUS_CHOICES, default="available")

    def __str__(self):
        return f"{self.table_number} is {self.status}"
    
class MenuItem(AbstractBaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} from {self.restaurant.name}"
