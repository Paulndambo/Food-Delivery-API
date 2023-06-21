from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from apps.orders.models import Order, OrderItem
from apps.orders.serializers import OrderSerializer
# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    #def create(self, request, *args, **kwargs):
    #    data = request.data
    #    serializer = self.serializer_class(data=data)
    #    if serializer.is_valid(raise_exception=True):
    #        order_items = serializer.validated_data["order_items"]
    #        print(order_items)
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
