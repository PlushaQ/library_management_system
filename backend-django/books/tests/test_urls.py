from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Author, Category, Tag, Series, Book


class TestUrls(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.author = Author.objects.create(name="Test Author", short_biography="Test Biography")
        self.category = Category.objects.create(name="Test Category")
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")
        self.series = Series.objects.create(name="Test Series")

        self.book1 = Book.objects.create(
            id=1,
            title="Test Book 1",
            author=self.author,
            description="Test Description 1",
            publication_date="2022-01-01",
            isbn="1234567890123",
            series=self.series,
            volume=1
        )
        self.book1.category.add(self.category)
        self.book1.tags.add(self.tag1, self.tag2)

    def test_book_list_url(self):
        url = reverse('books:book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail_url(self):
        url = reverse('books:book_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_filter_url(self):
        url = reverse('books:book_filter')
        response = self.client.get(url, {'author_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

