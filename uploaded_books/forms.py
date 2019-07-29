from django import forms
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)


class EBookForm(forms.ModelForm):
	class Meta:
		model = EBook
		exclude = ('name', )


class Book5x8Form(forms.ModelForm):
	class Meta:
		model = Book5x8
		exclude = ('name', )


class BookA5HardcoverForm(forms.ModelForm):
	class Meta:
		model = BookA5Hardcover
		exclude = ('name', )


class Book115x18FnskuForm(forms.ModelForm):
	class Meta:
		model = Book115x18Fnsku
		exclude = ('name', )


class Book115x18IsbnForm(forms.ModelForm):
	class Meta:
		model = Book115x18Isbn
		exclude = ('name', )


class Book125x19HardcoverForm(forms.ModelForm):
	class Meta:
		model = Book125x19Hardcover
		exclude = ('name', )


class Book125x19FnskuForm(forms.ModelForm):
	class Meta:
		model = Book125x19Fnsku
		exclude = ('name', )


class Book125x19IsbnForm(forms.ModelForm):
	class Meta:
		model = Book125x19Isbn
		exclude = ('name', )
