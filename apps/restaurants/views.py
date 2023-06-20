from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from rest_framework.response import Response


from apps.restaurants.models import Restaurant, RestaurantTable, MenuItem, TableBooking
from apps.restaurants.serializers import (
    RestaurantSerializer, 
    RestaurantTableSerializer,
    MenuItemSerializer,
    TableBookingSerializer
)

# Create your views here.
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantTableViewSet(ModelViewSet):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer


class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class TableBookingViewSet(ModelViewSet):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):

            """Check if table is available for booking"""
            table = serializer.validated_data["table"]
            if table.status.lower() == "booked":
                return Response({"failed": "The table you are trying to book is already booked" }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)