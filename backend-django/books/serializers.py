from rest_framework import serializers
from .models import Book, Author, Category, Tag, BookInstance, Series

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Serializes author data to and from JSON format.
    """
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model. Serializes category data to and from JSON format.
    """
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tag model. Serializes tag data to and from JSON format.
    """
    class Meta:
        model = Tag
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Series model. Serializes series data to and from JSON format.
    """
    class Meta:
        model = Series
        fields = '__all__'

class BookInstanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookInstance model. Serializes book instance data to and from JSON format.
    """
    class Meta:
        model = BookInstance
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. Serializes book data to and from JSON format, including nested serialization of related models.
    """
    author = AuthorSerializer()
    category = CategorySerializer(many=True)
    tags = TagSerializer(many=True)
    series = SeriesSerializer()

    class Meta:
        model = Book
        fields = '__all__'
