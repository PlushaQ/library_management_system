from rest_framework import serializers

from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Serializes author data to and from JSON format.
    """
    class Meta:
        model = Author
        fields = '__all__'