from rest_framework.serializers import ModelSerializer
from .models import NewUser


class RegisterUserSerializer(ModelSerializer):
    """
    Serializer for registering a new user.
    It takes user email, user_name and password and creates new user with provided data.
    
    """
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance