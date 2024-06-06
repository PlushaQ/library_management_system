from django.test import TestCase
from rest_framework.serializers import ValidationError
from ..models import AuthorCategory, AuthorTag
from ..serializers import AuthorSerializer, AuthorListSerializer, AuthorDetailsSerializer
from datetime import date

class AuthorSerializerTestCase(TestCase):

    def setUp(self):
        # Create tags and categories
        self.category1 = AuthorCategory.objects.create(name="Fiction")
        self.category2 = AuthorCategory.objects.create(name="Drama")
        self.tag1 = AuthorTag.objects.create(name="bestseller")
        self.tag2 = AuthorTag.objects.create(name="contemporary")

        # Define author short data 
        self.author_data = {
            'id': 1,
            'name': 'Test author'
        }

        # Define author data to lists
        self.author_list_data = {
            'id': 1,
            'name': 'Test author',
            'short_biography': 'An accomplished author...',
            'categories': [self.category1.id, self.category2.id],
            'tags': [self.tag1.id, self.tag2.id],
        }

        # Define detailed author's data
        self.author_details_data = {
            'id': 1,
            'name': 'Test author',
            'short_biography': 'An accomplished author...',
            'long_biography': 'A very detailed biography of Test author...',
            'birth_date': date(1970, 1, 1),
            'death_date': date(2020, 1, 1),
            'categories': [self.category1.id, self.category2.id],
            'tags': [self.tag1.id, self.tag2.id],
            'website': 'http://localhost:8000',
        }

    def test_author_serializer(self):
        """
        Ensure that AuthorSerializer works.
        """
        serializer = AuthorSerializer(data=self.author_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], self.author_data['name'])

    def test_author_list_serializer(self):
        """
        Ensure that AuthorListSerializer works.
        """
        serializer = AuthorListSerializer(data=self.author_list_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], self.author_list_data['name'])
        self.assertEqual(serializer.validated_data['short_biography'], self.author_list_data['short_biography'])
        self.assertEqual(
            [category.id for category in serializer.validated_data['categories']],
            self.author_list_data['categories']
        )
        self.assertEqual(
            [tag.id for tag in serializer.validated_data['tags']],
            self.author_list_data['tags']
        )
    def test_author_details_serializer_valid(self):
        """
        Ensure that AuthorDetailsSerializer works.
        """
        serializer = AuthorDetailsSerializer(data=self.author_details_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], self.author_details_data['name'])
        self.assertEqual(serializer.validated_data['birth_date'], self.author_details_data['birth_date'])
        self.assertEqual(serializer.validated_data['death_date'], self.author_details_data['death_date'])
        self.assertEqual(serializer.validated_data['long_biography'], self.author_details_data['long_biography'])
        self.assertEqual(serializer.validated_data['website'], self.author_details_data['website'])
        self.assertEqual(
            [category.id for category in serializer.validated_data['categories']],
            self.author_list_data['categories']
        )
        self.assertEqual(
            [tag.id for tag in serializer.validated_data['tags']],
            self.author_list_data['tags']
        )

    def test_author_details_serializer_invalid(self):
        """
        Ensure that AuthorDetailsSerializer rejects invalid data.
        """
        invalid_data = self.author_details_data.copy()
        invalid_data['birth_date'] = date(2021, 1, 1)  # Birth date is after death date
        serializer = AuthorDetailsSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertRaises(ValidationError)
