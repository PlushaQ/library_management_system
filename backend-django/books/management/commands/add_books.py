import random
import string
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from books.models import Book, Category, Tag, Series
from authors.models import Author  # Adjust the import as necessary
from django.utils.text import slugify
from uuid import uuid4

class Command(BaseCommand):
    help = 'Add 100 books to the database'

    def handle(self, *args, **kwargs):
        # Create authors if none exist
        if not Author.objects.exists():
            self.stdout.write(self.style.WARNING('No authors found. Creating sample authors...'))
            self.create_authors()

        # Create categories if none exist
        if not Category.objects.exists():
            self.stdout.write(self.style.WARNING('No categories found. Creating sample categories...'))
            self.create_categories()

        authors = Author.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        series = Series.objects.all()

        for i in range(100):
            author = random.choice(authors)
            title = f'Book {i+1}'
            description = f'This is the description for book {i+1}.'
            publication_date = datetime.now() - timedelta(days=random.randint(0, 365*10))
            isbn = ''.join(random.choices(string.digits, k=13))

            book = Book.objects.create(
                title=title,
                author=author,
                description=description,
                publication_date=publication_date.date(),
                isbn=isbn,
                slug=slugify(title) + '-' + str(uuid4())[:4],
            )

            # Add categories
            book.category.set(random.sample(list(categories), random.randint(1, len(categories))))

            # Add tags
            book.tags.set(random.sample(list(tags), random.randint(1, len(tags))))

            # Optionally add series
            if series.exists():
                if random.choice([True, False]):
                    book.series = random.choice(series)
                    book.volume = random.randint(1, 10)

            book.save()

        self.stdout.write(self.style.SUCCESS('Successfully added 100 books.'))

    def create_authors(self):
        sample_authors = [
            {'name': 'John Doe'},
            {'name': 'Jane Smith'},
            {'name': 'Michael Johnson'},
            {'name': 'Emily Brown'},
            # Add more sample authors as needed
        ]

        for author_data in sample_authors:
            Author.objects.create(name=author_data['name'])

    def create_categories(self):
        sample_categories = [
            {'name': 'Fiction'},
            {'name': 'Science Fiction'},
            {'name': 'Fantasy'},
            {'name': 'Romance'},
            # Add more sample categories as needed
        ]

        for category_data in sample_categories:
            Category.objects.create(name=category_data['name'])

