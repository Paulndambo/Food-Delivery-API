from django.shortcuts import render

"""Rest Framework Imports"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response

"""Filter Backend Imports"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

"""Models Imports"""
from apps.restaurants.models import Restaurant, RestaurantTable, MenuItem, TableBooking

"""Serializers Imports"""
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
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "town", "country"]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:
            existing_restaurant = Restaurant.objects.filter(owner=user)
            if existing_restaurant:
                return Response({"failed": "A user can only own one restaurant" }, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantTableViewSet(ModelViewSet):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["status", "table_number", "restaurant__name"]
    

class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "restaurant__name"]


class TableBookingViewSet(ModelViewSet):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["booking_status", "booked_from", "booked_up_to"]

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
    

    def get_queryset(self):
        user = self.request.user
        if user.role.lower() == "customer":
            return self.queryset.filter(user=user)
        elif user.role.lower() == "restaurant":
            return self.queryset.filter(table__restaurant__owner=user)
        elif user.role.lower() in ["admin", "customer_service"] or user.is_superuser:
            return self.queryset 