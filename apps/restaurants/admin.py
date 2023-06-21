from django.contrib import admin
from apps.restaurants.models import Restaurant, RestaurantTable, TableBooking, MenuItem
# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["owner", "name", "town", "country"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "name", "quantity", "price", "discount"]

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = ["table_number", "restaurant", "capacity", "status"]

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ["user", "table", "booked_from", "booked_up_to", "booking_status"]