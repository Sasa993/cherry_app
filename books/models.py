from django.db import models
# from django.forms import ModelForm
from django import forms
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth.models import User
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)
# from django.conf import settings
# import os


class Author(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name} {self.last_name}"


class Book(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	working_number = models.PositiveIntegerField()
	description = models.TextField(blank=True)
	comparible = models.URLField(max_length=200, blank=True)
	co_author_name = models.ManyToManyField(Author, related_name='co_author')
	# co_author_email = models.CharField(max_length=100)
	# co_author_email = models.ManyToManyField(Author, related_name='co_author_email')
	co_author_instructions = models.TextField(blank=True)
	author = models.ManyToManyField(Author, related_name='author')
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	modified_at = models.DateTimeField(auto_now=True, blank=True)
	cover = models.ImageField(upload_to='cover_image/', blank=True)
	ebook = models.ForeignKey(EBook, on_delete=models.SET_NULL, blank=True, null=True)
	book5x8 = models.ForeignKey(Book5x8, on_delete=models.SET_NULL, blank=True, null=True)
	book_A5_hardcover = models.ForeignKey(BookA5Hardcover, on_delete=models.SET_NULL, blank=True, null=True)
	book_115x18_fnsku = models.ForeignKey(Book115x18Fnsku, on_delete=models.SET_NULL, blank=True, null=True)
	book_115x18_isbn = models.ForeignKey(Book115x18Isbn, on_delete=models.SET_NULL, blank=True, null=True)
	book_125x19_hardcover = models.ForeignKey(Book125x19Hardcover, on_delete=models.SET_NULL, blank=True, null=True)
	book_125x19_fnsku = models.ForeignKey(Book125x19Fnsku, on_delete=models.SET_NULL, blank=True, null=True)
	book_125x19_isbn = models.ForeignKey(Book125x19Isbn, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return f"{self.title}"


class BookRequest(models.Model):
	authors_accepted = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)
	book = models.ForeignKey('Book', on_delete=models.CASCADE,)
	deadline = models.DateField(blank=True, null=True)
	decision = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.book}"


class BookForm(forms.ModelForm):
	author = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all(), required=False)
	co_author_name = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all(), required=False)

	class Meta:
		model = Book
		fields = '__all__'
		# widgets = {
		# 	'author': Select2MultipleWidget,
		# 	'co_author_name': Select2MultipleWidget
		# }
