from django.db import models
from utils.custom_upload_path import CustomUploadPath
from django.template.defaultfilters import slugify
from uuid import uuid4

from authors.models import Author

class Category(models.Model):
    """
    Represents a category for grouping related content.
    :param name: The name of the category
    :returns: String respresentation of the category.
    """
    name = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    """
    Represents a tag for categorizing or labeling content.

    :param name: The name of the tag.
    :returns: String representation of the tag.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Series(models.Model):
    """
    Represents a series of books.

    :param name: The name of the series.
    :param description: Description of the series (optional).
    :returns: String representation of the series.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


upload_to = CustomUploadPath('books/covers')

class Book(models.Model):
    """
    Represents a book.

    :param title: The title of the book.
    :param author: The author of the book.
    :param cover: The cover image of the book.
    :param description: Description of the book.
    :param category: The category of the book (optional).
    :param publication_date: Publication date of the book.
    :param isbn: ISBN of the book.
    :param tags: Tags associated with the book (optional).
    :param edition: Edition of the book (optional).
    :param series: The series to which the book belongs (optional).
    :param volume: The volume number if part of a series (optional).
    :returns: String representation of the book.
    """

    title = models.TextField(max_length=255, blank=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    cover = models.ImageField(
        upload_to=upload_to,
        default='/books/covers/default.jpg',
        )
    description = models.TextField(max_length=5000)
    category = models.ManyToManyField(Category, blank=True)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    tags = models.ManyToManyField(Tag, blank=True)
    edition = models.CharField(max_length=50, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + '-' + uuid4()[:4]
        super().save(self, *args, **kwargs)
    
class BookInstance(models.Model):
    """
    Represents an instance of a book.

    :param book: The book associated with the instance.
    :param condition: The condition of the book instance.
    :param availability_status: The availability status of the book instance.
    :returns: String representation of the book instance.
    """
    CONDITION_CHOICES = (
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('acceptable', 'Acceptable'),
    )

    AVAILABLE_CHOICES = (
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
        ('reserved', 'Reserved'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='instances')
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    availability_status = models.CharField(max_length=20, choices=AVAILABLE_CHOICES, default='available')

    def __str__(self):
        return f"{self.book.title} - {self.condition} - {self.availability_status}"    