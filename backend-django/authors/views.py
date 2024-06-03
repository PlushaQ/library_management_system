from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Author
from .serializers import AuthorDetailsSerializer, AuthorListSerializer


class AuthorList(generics.ListAPIView):
    """
    A view for retrieving a list of authors filtered by tag or category.

    This view allows any user to retrieve a list of authors based on specified filters.
    """
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer

    def get_queryset(self):
        queryset = Author.objects.all() 
        
        # Retrieve query parameters for filtering
        tag_id = self.request.query_params.get('tag_id')
        category_id = self.request.query_params.get('category_id')

        # Apply filters if provided
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        if category_id:
            queryset = queryset.filter(categories__id=category_id)
        
        return queryset
    
class AuthorDetail(generics.RetrieveAPIView):
    """
    A view for retrieving a detailed author data.

    This view allows any user to retrieve full data about Author.
    """
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorDetailsSerializer



 

