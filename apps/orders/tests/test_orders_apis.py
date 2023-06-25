from unittest import TestCase
from django.test import Client
from django.urls import reverse
import json
import pytest
from .models import Order, OrderItem


pytestmark = pytest.mark.django_db

class BaseOrderTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.orders_url = reverse("orders-list")
    
    def tearDown(self) -> None:
        pass


class BaseOrderItemTeCase(TestCase):
    pass


class TestGetOrders(BaseOrderTestCase):
    def test_unauthorized_should_return_error(self):
        response = self.client.get(self.orders_url)
        self.assertEqual(response.status_code, 401)