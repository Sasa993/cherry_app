from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Author, Book, BookRequest

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Permission)
admin.site.register(BookRequest)

# admin.site.register(EBook)
