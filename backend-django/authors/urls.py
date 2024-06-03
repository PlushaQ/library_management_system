from django.urls import path
from .views import AuthorList, AuthorDetail

app_name = 'authors'

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
]
