from rest_framework import serializers

from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Serializes author general data to and from JSON format.
    """
    class Meta:
        model = Author
        fields = ('id', 'name')

class AuthorDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model. Serializes full author data to and from JSON format
    """
    class Meta:
        model = Author
        fields = '__all__'