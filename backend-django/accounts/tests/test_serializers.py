from rest_framework.test import APITestCase
from ..serializers import RegisterUserSerializer


class RegisterUserSerializerTests(APITestCase):
    def test_serializer_valid_data(self):
        data = {'email': 'test@example.com', 'user_name': 'test_user', 'password': 'testpassword'}
        serializer = RegisterUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_serializer_invalid_data(self):
        data = {'email': 'invalid_email', 'user_name': 'test_user', 'password': 'testpassword'}
        serializer = RegisterUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        
    def test_serializer_create_user(self):
        data = {'email': 'test@example.com', 'user_name': 'test_user', 'password': 'testpassword'}
        serializer = RegisterUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertIsNotNone(instance)
        self.assertEqual(instance.email, 'test@example.com')