from django.test import TestCase
from ..models import Book, Author, Category, Tag, Series
from ..serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.category1 = Category.objects.create(name="Test Category 1")
        self.category2 = Category.objects.create(name="Test Category 2")
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")
        self.series = Series.objects.create(name="Test Series")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            series=self.series,
            publication_date='2024-05-06',
        )
        self.book.tags.add(self.tag1, self.tag2)
        self.book.category.add(self.category1, self.category2)

        # Book serializer
        self.book_serializer = BookSerializer(instance=self.book)
        self.serialized_data = self.book_serializer.data

    def test_book_serialization(self):
        self.assertIn('title', self.serialized_data)
        self.assertIn('author', self.serialized_data)
        self.assertIn('category', self.serialized_data)
        self.assertIn('series', self.serialized_data)
    
    def test_book_serialized_data(self):
        self.assertEqual(self.serialized_data['title'], self.book.title)
        self.assertEqual(self.serialized_data['author']['id'], self.book.author.id)

        serialized_category_ids = [category['id'] for category in self.serialized_data['category']]
        category_ids = [category.id for category in self.book.category.all()]
        self.assertEqual(set(serialized_category_ids), set(category_ids))

        self.assertEqual(self.serialized_data['series']['id'], self.book.series.id)
    
    def test_book_many_to_many_fields(self):
        self.assertEqual(len(self.serialized_data['tags']), self.book.tags.count())
        self.assertEqual(len(self.serialized_data['category']), self.book.category.count())

    def test_book_related_serializers(self):
        self.assertIn('series', self.serialized_data)
        self.assertEqual(self.serialized_data['series']['name'], self.book.series.name)
        self.assertIn('author', self.serialized_data)
        self.assertEqual(self.serialized_data['author']['name'], self.book.author.name)

    def test_book_validation(self):
        invalid_data = {'title': '', 'author': '', 'series': ''}
        serializer = BookSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
        self.assertIn('author', serializer.errors)
        self.assertIn('series', serializer.errors)