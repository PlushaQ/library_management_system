from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from urllib.parse import urlparse

from ..models import Author, AuthorTag, AuthorCategory
from ..serializers import AuthorDetailsSerializer, AuthorListSerializer

class AuthorTests(APITestCase):
    
    def setUp(self):
        self.category1 = AuthorCategory.objects.create(name="Fiction")
        self.category2 = AuthorCategory.objects.create(name="Non-Fiction")
        self.tag1 = AuthorTag.objects.create(name="Bestseller")
        self.tag2 = AuthorTag.objects.create(name="Debut")

        self.author1 = Author.objects.create(
            name="Author One",
            short_biography="Short bio of Author One",
            long_biography="Long bio of Author One",
            birth_date="1970-01-01",
            death_date=None,
            website="http://authorone.com",
        )
        self.author2 = Author.objects.create(
            name="Author Two",
            short_biography="Short bio of Author Two",
            long_biography="Long bio of Author Two",
            birth_date="1980-01-01",
            death_date=None,
            website="http://authortwo.com",
        )

        self.author1.categories.add(self.category1)
        self.author1.tags.add(self.tag1)
        self.author2.categories.add(self.category2)
        self.author2.tags.add(self.tag2)
        
        self.list_url = reverse('authors:author_list')
        self.detail_url = lambda pk: reverse('authors:author_detail', args=[pk]) 

    def test_author_list(self):
        """
        Ensure we can retrieve the list of authors.
        """
        response = self.client.get(self.list_url)
        authors = Author.objects.all()
        serializer = AuthorListSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = [{**item, 'photo': urlparse(item['photo']).path} for item in response.data]
        self.assertEqual(response_data, serializer.data)
        
    def test_author_list_with_tag_filter(self):
        """
        Ensure we can filter the list of authors by tag.
        """
        response = self.client.get(self.list_url, {'tag_id': self.tag1.id})
        authors = Author.objects.filter(tags__id=self.tag1.id)
        serializer = AuthorListSerializer(authors, many=True)
        
        # Remove the domain part from photo URLs in response data
        response_data = [{**item, 'photo': urlparse(item['photo']).path} for item in response.data]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, serializer.data)
        
    def test_author_list_with_category_filter(self):
        """
        Ensure we can filter the list of authors by category.
        """
        response = self.client.get(self.list_url, {'category_id': self.category1.id})
        authors = Author.objects.filter(categories__id=self.category1.id)
        serializer = AuthorListSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = [{**item, 'photo': urlparse(item['photo']).path} for item in response.data]
        self.assertEqual(response_data, serializer.data)
        
    def test_author_detail(self):
        """
        Ensure we can retrieve a single author's details.
        """
        response = self.client.get(self.detail_url(self.author1.id))
        author = Author.objects.get(id=self.author1.id)
        serializer = AuthorDetailsSerializer(author)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response_data = [{**item, 'photo': urlparse(item['photo']).path} for item in response.data]
        self.assertEqual(response_data, serializer.data)
        
    def test_author_detail_not_found(self):
        """
        Ensure 404 is returned when author is not found.
        """
        response = self.client.get(self.detail_url(999))  # Assuming 999 does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
