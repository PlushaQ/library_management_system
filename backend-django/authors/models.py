from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Represents an author who writes content.

    :param name: The name of the author.
    :param short_biography: A brief biography or description of the author.
    :returns: String representation of the author.
    """
    name = models.TextField(max_length=100)
    short_biography = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name
