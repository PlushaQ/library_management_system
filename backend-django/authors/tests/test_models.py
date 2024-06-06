from django.test import TestCase
from ..models import Author, AuthorTag, AuthorCategory

class AuthorModelTests(TestCase):
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
            website="http://authorone.com",
            photo='/authors/photos/authorone.jpg',
        )
        self.author2 = Author.objects.create(
            name="Author Two",
            short_biography="Short bio of Author Two",
            long_biography="Long bio of Author Two",
            birth_date="1980-01-01",
            website="http://authortwo.com",
            photo='/authors/photos/authortwo.jpg',
        )

        self.author1.categories.add(self.category1)
        self.author1.tags.add(self.tag1)
        self.author2.categories.add(self.category2)
        self.author2.tags.add(self.tag2)

    def test_author_creation(self):
        """
        Ensure that authors are created correctly.
        """
        author1 = Author.objects.get(name="Author One")
        author2 = Author.objects.get(name="Author Two")
        self.assertEqual(author1.short_biography, "Short bio of Author One")
        self.assertEqual(author2.short_biography, "Short bio of Author Two")
        self.assertEqual(author1.photo, '/authors/photos/authorone.jpg')

    def test_author_categories(self):
        """
        Ensure that categories are added to authors correctly.
        """
        author1 = Author.objects.get(name="Author One")
        self.assertIn(self.category1, author1.categories.all())

    def test_author_tags(self):
        """
        Ensure that tags are added to authors correctly.
        """
        author1 = Author.objects.get(name="Author One")
        self.assertIn(self.tag1, author1.tags.all())

    def test_str_methods(self):
        """
        Ensure the string representation of models.
        """
        self.assertEqual(str(self.category1), "Fiction")
        self.assertEqual(str(self.tag1), "Bestseller")
        self.assertEqual(str(self.author1), "Author One")

