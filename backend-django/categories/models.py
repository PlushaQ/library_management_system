from django.db import models

# Create your models here.
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