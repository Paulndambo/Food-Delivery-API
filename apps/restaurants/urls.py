from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.restaurants.views import (
    RestaurantViewSet,
    RestaurantTableViewSet,
    MenuItemViewSet,
    TableBookingViewSet
)

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurants")
router.register("restaurant-tables", RestaurantTableViewSet, basename="restaurant-tables")
router.register("menu-items", MenuItemViewSet, basename="menu-items")
router.register("table-bookings", TableBookingViewSet, basename="table-bookings")

urlpatterns = [
    path("", include(router.urls)),
]
