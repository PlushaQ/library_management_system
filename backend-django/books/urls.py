from django.urls import path

from .views import BookList, BookDetail, BookByFilter

app_name = 'books'

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('books/filter/', BookByFilter.as_view(), name='book_filter'), 
]