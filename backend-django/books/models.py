from django.db import models

from uuid import uuid4

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.TextField(max_length=100)
    short_biography = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def upload_to(filename):
    return '/books/covers/{}'.format(filename + uuid4()[:8]),


class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField(max_length=255, blank=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    cover = models.ImageField(
        upload_to=upload_to,
        default='/books/covers/default.jpg',
        )
    description = models.TextField(max_length=5000)
    category = models.ManyToManyField(Category, default=1)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    tags = models.ManyToManyField(Tag, blank=True)
    edition = models.CharField(max_length=50, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
    
class BookInstance(models.Model):
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