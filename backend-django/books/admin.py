from django.contrib import admin
from .models import Book, Tag, Category, BookInstance, Series
# Register your models here.

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(BookInstance)
admin.site.register(Series)