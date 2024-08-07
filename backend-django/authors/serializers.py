from rest_framework import serializers

from .models import Author, AuthorCategory, AuthorTag

class AuthorCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the AuthorCategory model.
    """
    class Meta:
        model = AuthorCategory
        fields = ('id', 'name')

class AuthorTagSerializer(serializers.ModelSerializer):
    """
    Serializer for the AuthorTag model.
    """
    class Meta:
        model = AuthorTag
        fields = ('id', 'name')

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. Serializes author general data to and from JSON format.
    """
    class Meta:
        model = Author
        fields = ('id', 'name')

class AuthorListSerializer(serializers.ModelSerializer):
    """
    Serialzier for the Author model. Serializes data for list item to and from JSON format.
    Includes related categories and tags.
    """
    categories = AuthorCategorySerializer(many=True, read_only=True)
    tags = AuthorTagSerializer(many=True, read_only=True)
    photo = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Author
        fields = ('id', 'name', 'short_biography', 'categories', 'tags', 'photo')


class AuthorDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model. Serializes full author data to and from JSON format.
    Includes related categories and tags.
    """
    categories = AuthorCategorySerializer(many=True, read_only=True)
    tags = AuthorTagSerializer(many=True, read_only=True)
    photo = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Author
        fields = '__all__'

    def validate(self, data):
        """
        Validate that the birth date is before the death date.
        """
        if 'birth_date' in data and 'death_date' in data:
            if data['birth_date'] > data['death_date']:
                raise serializers.ValidationError('Birth date must be before death date.')
        return data
