from django.utils.deconstruct import deconstructible
from uuid import uuid4


@deconstructible
class CustomUploadPath:
    """
    Generates upload path for image files.

    :param filename: Name of the file.
    :returns: Upload path for the book cover.
    """
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid4().hex}.{ext}"
        return f"{self.sub_path}/{filename}"
