from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from rest_framework.response import Response


from apps.restaurants.models import Restaurant, RestaurantTable, MenuItem
from apps.restaurants.serializers import (
    RestaurantSerializer, 
    RestaurantTableSerializer,
    MenuItemSerializer
)

# Create your views here.
class RestaurantAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

class RestaurantRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    lookup_field = "pk"

class RestaurantTableAPIView(generics.ListCreateAPIView):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer


class RestaurantTableRestaurantRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer
    
    lookup_field = "pk"


class MenuItemAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    lookup_field = "pk"