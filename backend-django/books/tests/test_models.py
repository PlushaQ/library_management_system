from django.test import TestCase
from ..models import Category, Author, Tag, Series, Book, BookInstance
from datetime import date

class BookModelsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.author = Author.objects.create(name="Test Author", short_biography="Test biography")
        self.tag1 = Tag.objects.create(name="Test Tag 1")
        self.tag2 = Tag.objects.create(name="Test Tag 2")
        self.series = Series.objects.create(name="Test Series", description="Test series description")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            cover='books/covers/default.jpg',
            description="Test description",
            publication_date=date.today(),
            isbn="9780123456789",
            edition="First Edition",
            series=self.series,
            volume=1
        )
        self.book.category.add(self.category)
        self.book.tags.add(self.tag1, self.tag2)
        self.book_instance = BookInstance.objects.create(
            book=self.book,
            condition='new',
            availability_status='available'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Test Author")
        self.assertEqual(self.author.short_biography, "Test biography")

    def test_tag_creation(self):
        self.assertEqual(self.tag1.name, "Test Tag 1")
        self.assertEqual(self.tag2.name, "Test Tag 2")

    def test_series_creation(self):
        self.assertEqual(self.series.name, "Test Series")
        self.assertEqual(self.series.description, "Test series description")

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, self.author)
        self.assertEqual(self.book.cover, 'books/covers/default.jpg')
        self.assertEqual(self.book.description, "Test description")
        self.assertIn(self.category, self.book.category.all())
        self.assertEqual(self.book.publication_date, date.today())
        self.assertEqual(self.book.isbn, "9780123456789")
        self.assertEqual(self.book.edition, "First Edition")
        self.assertEqual(self.book.series, self.series)
        self.assertEqual(self.book.volume, 1)
        self.assertIn(self.tag1, self.book.tags.all())
        self.assertIn(self.tag2, self.book.tags.all())

    def test_book_instance_creation(self):
        self.assertEqual(self.book_instance.book, self.book)
        self.assertEqual(self.book_instance.condition, 'new')
        self.assertEqual(self.book_instance.availability_status, 'available')
