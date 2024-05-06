from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Book, Author, Category, Tag, Series

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'  # Reset to default color


class BookViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.author = Author.objects.create(name="Test Author", short_biography="Test Biography")
        self.category = Category.objects.create(name="Test Category")
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")
        self.series = Series.objects.create(name="Test Series")

        self.book1 = Book.objects.create(
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

        self.book2 = Book.objects.create(
            title="Test Book 2",
            author=self.author,
            description="Test Description 2",
            publication_date="2022-02-01",
            isbn="9876543210987",
        )

    def test_get_book_list(self):
        url = reverse('books:book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        url = reverse('books:book_detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book 1")

    def test_filter_books_by_author(self):
        url = reverse('books:book_filter')
        response = self.client.get(url, {'author_id': self.author.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_category(self):
        url = reverse('books:book_filter')
        response = self.client.get(url, {'category_id': self.category.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book 1")

    def test_filter_books_by_tag(self):
        url = reverse('books:book_filter')
        response = self.client.get(url, {'tag_id': self.tag1.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book 1")

    def test_filter_books_by_series(self):
        url = reverse('books:book_filter')
        response = self.client.get(url, {'series_id': self.series.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book 1")