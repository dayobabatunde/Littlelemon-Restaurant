# tests/test_views.py
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Auth setup
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="apitester",
            password="pass1234"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        # Test data
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=12, inventory=50)
        Menu.objects.create(title="Burger", price=10, inventory=30)

        # If you prefer reversing, give your URL a name; otherwise hit the path directly:
        self.url = "/restaurant/menu/"

    def test_getall(self):
        response = self.client.get(self.url)

        # Should be authorized OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # What we *expect* back
        queryset = Menu.objects.all().order_by("id")
        expected = MenuSerializer(queryset, many=True).data

        # Handle both paginated and non-paginated responses
        payload = response.data.get("results", response.data) if isinstance(response.data, dict) else response.data

        self.assertEqual(payload, expected)
