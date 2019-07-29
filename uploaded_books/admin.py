from django.contrib import admin

from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)

admin.site.register(EBook)
admin.site.register(Book5x8)
admin.site.register(BookA5Hardcover)
admin.site.register(Book115x18Fnsku)
admin.site.register(Book115x18Isbn)
admin.site.register(Book125x19Hardcover)
admin.site.register(Book125x19Fnsku)
admin.site.register(Book125x19Isbn)
