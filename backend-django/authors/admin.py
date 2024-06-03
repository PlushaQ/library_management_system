from django.contrib import admin
from .models import Author, AuthorCategory, AuthorTag
# Register your models here.

admin.site.register(Author)
admin.site.register(AuthorCategory)
admin.site.register(AuthorTag)