from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken 


class CustomUserCreate(APIView):
    """
    View for user registration.

    This view handles the registration of a new user by accepting
    POST requests with user information. It uses the RegisterUserSerializer
    to validate and create a new user instance.

    Permissions:
        - AllowAny: Anyone can register a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                data = {'message': 'Account created successfully.'}
                return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BlacklistTokenView(APIView):
    """
    View for blacklisting refresh tokens.

    This view handles the blacklisting of refresh tokens by accepting
    POST requests with the refresh token. It blacklists the token using
    the RefreshToken class from rest_framework_simplejwt.

    Permissions:
        - AllowAny: Anyone can blacklist a refresh token.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)