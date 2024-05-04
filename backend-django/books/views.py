from rest_framework import generics
from rest_framework.permissions import AllowAny



from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
