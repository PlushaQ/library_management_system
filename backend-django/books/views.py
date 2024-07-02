from rest_framework import generics
from rest_framework.permissions import AllowAny


from .models import Book
from .serializers import BookSerializer
from utils.paginator import CustomPagination
# Create your views here.


class BookList(generics.ListAPIView):
    """
    A view for retrieving a list of books.

    This view allows any user to retrieve a list of books.
    """
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class BookDetail(generics.RetrieveAPIView):
    """
    A view for retrieving details of a book.

    This view allows any user to retrieve details of a specific book.
    """
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookByFilter(generics.ListAPIView):
    """
    A view for retrieving a list of books filtered by author, tag, or category.

    This view allows any user to retrieve a list of books based on specified filters.
    """
    permission_classes = [AllowAny] 
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Book.objects.all() 
        
        # Retrieve query parameters for filtering
        author_id = self.request.query_params.get('author_id')
        tag_id = self.request.query_params.get('tag_id')
        category_id = self.request.query_params.get('category_id')
        series_id = self.request.query_params.get('series_id')

        # Apply filters if provided
        if author_id:
            queryset = queryset.filter(author__id=author_id)
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        if series_id:
            queryset = queryset.filter(series__id=series_id)
        
        return queryset