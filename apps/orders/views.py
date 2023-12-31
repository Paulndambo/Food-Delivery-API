from django.shortcuts import render

"""Rest Framework Imports"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

"""Filter Backend Imports"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

"""Models Imports"""
from apps.orders.models import Order, OrderItem

"""Serializers Imports"""
from apps.orders.serializers import OrderSerializer
# Create your views here.
class OrderViewSet(ModelViewSet):
    """
    : Order model maps to the Order table on the db,
    : Orders endpoint should be protected since the response data is specific to;-
    :   -> Customer
    :   -> Restaurant
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["payment_status", "order_status", "restaurant__name", "customer__user__email"]

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_queryset(self):
        """
        : From the current request, get the authenticated user
        : Specific user role determines the orders data they will get upon a get request
        : -> Customer, only gets data on order they have made
        : -> Restaurant, only gets data on orders made on the specific restaurant
        : -> Admin, This user can get all order data on orders
        """
        user = self.request.user

        if user.role.lower() == "customer":
            return self.queryset.filter(customer__user=user)
        elif user.role.lower() == "restaurant":
            return self.queryset.filter(restaurant__user=user)
        elif user.role.lower() in ["admin", "customer_service"] or user.is_superuser:
            return self.queryset

