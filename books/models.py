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
	# co_author_email = models.CharField(max_length=100)
	co_author_email = models.ManyToManyField(Author, related_name='co_author_email')
	co_author_instructions = models.TextField()
	# author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
	author = models.ManyToManyField(Author, related_name='author')
	cover = models.ImageField(upload_to='cover_image/', blank=False)

	def __str__(self):
		return f"{self.title}"


class BookForm(forms.ModelForm):
	author = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all())
	co_author_name = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all())
	# co_author_name = forms.ModelChoiceField(queryset=Author.objects.all())
	# co_author_email = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all())
	# co_author_email = forms.CharField(required=False)

	class Meta:
		model = Book
		fields = ('title', 'subtitle', 'description', 'comparible', 'co_author_name', 'co_author_email', 'co_author_instructions', 'author', 'cover')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['co_author_email'].queryset = Author.objects.none()

		# SKONTAJ
		if('authorId' in self.data):
			try:
				country_id = int(self.data.get('authorId'))
				self.fields['co_author_email'].queryset = Author.objects.filter(author_id=country_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif(self.instance.pk):
			self.fields['co_author_email'].queryset = self.instance.authorId.co_author_email_set
