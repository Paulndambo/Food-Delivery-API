from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.users.models import Customer
from apps.users.serializers import CustomerSerializer


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer