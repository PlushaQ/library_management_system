from django.contrib import admin
from .models import Book, Tag, Author, Category, BookInstance, Series
# Register your models here.

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BookInstance)
admin.site.register(Series)