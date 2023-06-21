from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.users.models import Customer, User
from apps.users.serializers import CustomerSerializer, UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer