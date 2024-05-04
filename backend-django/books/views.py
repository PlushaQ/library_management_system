from rest_framework import generics
from rest_framework.permissions import AllowAny


from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookList(generics.ListAPIView):
    """
    A view for retrieving a list of books.

    This view allows any user to retrieve a list of books.
    """
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    """
    A view for retrieving details of a book.

    This view allows any user to retrieve details of a specific book.
    """
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer