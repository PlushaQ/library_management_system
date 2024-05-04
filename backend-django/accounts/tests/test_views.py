from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import NewUser


class CustomUserCreateTests(APITestCase):
    def test_create_user(self):
        url = reverse('accounts:create_user')
        data = {'email': 'test@example.com', 'user_name': 'test_user', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NewUser.objects.count(), 1)
        self.assertEqual(NewUser.objects.get().email, 'test@example.com')