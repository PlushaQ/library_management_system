from django.db import models
from utils.custom_upload_path import CustomUploadPath

# Create your models here.

upload_to = CustomUploadPath('books/covers')

class Author(models.Model):
    """
    Represents an author who writes content.

    :param name: The name of the author.
    :param short_biography: A brief biography or description of the author.
    :param long_biography: A detailed biography of the author.
    :param birth_date: The birth date of the author.
    :param death_date: The death date of the author (if applicable).
    :param categories: Categories associated with the author.
    :param tags: Tags associated with the author.
    :param website: The personal or professional website of the author.
    :param photo: A profile picture or portrait of the author.
    :returns: String representation of the author.
    """
    name = models.CharField(max_length=100, unique=True)
    short_biography = models.TextField(max_length=1000)
    long_biography = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    main_genre = models.CharField(blank=True, null=True)
    website = models.URLField(null=True, blank=True)
    photo = models.ImageField(
        upload_to=upload_to,
        default='/authors/photos/default.jpg',
        )
    
    
    class Meta:
        ordering = ('name', )
    
    def __str__(self) -> str:
        return self.name
