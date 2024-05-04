from django.urls import path

from .views import BookList

app_name = 'books'

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list')
]