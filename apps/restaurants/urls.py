from django.urls import path 
from apps.restaurants.views import (
    RestaurantAPIView,
    RestaurantRetrieveUpdateDeleteAPIView,
    RestaurantTableAPIView,
    RestaurantTableRestaurantRetrieveUpdateDeleteAPIView,
    MenuItemAPIView,
    MenuItemRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path("", RestaurantAPIView.as_view(), name="restaurants"),
    path("<int:pk>/", RestaurantRetrieveUpdateDeleteAPIView.as_view(), name="restaurants"),
    path("restaurant-tables/", RestaurantTableAPIView.as_view(), name="restaurant-tables"),
    path("restaurant-tables/<int:pk>/", RestaurantTableRestaurantRetrieveUpdateDeleteAPIView.as_view(), name="restaurant-tables"),
    path("menu-items/", MenuItemAPIView.as_view(), name="menu-items"),
    path("menu-items/<int:pk>/", MenuItemRetrieveUpdateDeleteAPIView.as_view(), name="menu-items"),
]
