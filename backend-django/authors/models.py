from django.db import models
from utils.custom_upload_path import CustomUploadPath

# Create your models here.

upload_to = CustomUploadPath('books/covers')

class Author(models.Model):
    """
    Represents an author who writes content.

    :param name: The name of the author.
    :param short_biography: A brief biography or description of the author.
    :returns: String representation of the author.
    """
    name = models.TextField(max_length=100)
    short_biography = models.TextField(max_length=1000)
    photo = models.ImageField(
        upload_to=upload_to,
        default='/books/covers/default.jpg',
        )
    
    def __str__(self) -> str:
        return self.name
