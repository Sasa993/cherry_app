from django.db import models
# from django.forms import ModelForm
from django import forms
from django_select2.forms import Select2MultipleWidget


class Author(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return (f"{self.name} {self.last_name}")


class Book(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	description = models.TextField()
	comparible = models.URLField(max_length=200)
	co_author_name = models.ManyToManyField(Author, related_name='co_author')
	co_author_email = models.CharField(max_length=100)
	co_author_instructions = models.TextField()
	# multiple should be possible, so use multiselectfield - https://pypi.org/project/django-multiselectfield/ - https://www.youtube.com/watch?v=5jWJBpS0tkg
	# author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
	author = models.ManyToManyField(Author, related_name='author')
	cover = models.ImageField(upload_to='cover_image/', blank=False)

	def __str__(self):
		return f"{self.title}"


class BookForm(forms.ModelForm):
	author = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all())
	co_author_name = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all())

	class Meta:
		model = Book
		fields = '__all__'
