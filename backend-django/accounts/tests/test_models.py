from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'user_name': 'testuser',
            'first_name': 'Test',
            'password': 'testpassword'
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.user_name, self.user_data['user_name'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser_data = {**self.user_data, 'is_staff': True, 'is_superuser': True}
        user = User.objects.create_superuser(**superuser_data)
        self.assertEqual(user.email, superuser_data['email'])
        self.assertEqual(user.user_name, superuser_data['user_name'])
        self.assertEqual(user.first_name, superuser_data['first_name'])
        self.assertTrue(user.check_password(superuser_data['password']))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_missing_email(self):
        user_data = self.user_data.copy()
        user_data['email'] = None
        with self.assertRaises(ValueError):
            User.objects.create_user(**user_data)

    def test_create_superuser_missing_email(self):
        user_data = {**self.user_data, 'is_staff': True, 'is_superuser': True}
        user_data['email'] = None
        with self.assertRaises(ValueError):
            User.objects.create_superuser(**user_data)

    def test_create_superuser_not_staff(self):
        user_data = {**self.user_data, 'is_staff': False}
        with self.assertRaises(ValueError):
            User.objects.create_superuser(**user_data)

    def test_create_superuser_not_superuser(self):
        user_data = {**self.user_data, 'is_superuser': False}
        with self.assertRaises(ValueError):
            User.objects.create_superuser(**user_data)

    def test_unique_email_and_username(self):
        User.objects.create_user(**self.user_data)
        duplicate_data = {
            'email': 'test@example.com',
            'user_name': 'testuser_duplicate',
            'first_name': 'Test',
            'password': 'testpassword'
        }
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**duplicate_data)