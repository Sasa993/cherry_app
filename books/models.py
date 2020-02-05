from django.db import models
from django import forms
# from django.dispatch import receiver
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth.models import User
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)
from .validators import (
	validate_underscore, validate_digits_after_underscore, validate_alpha_before_underscore, validate_two_letters)
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.conf import settings
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Author(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name} {self.last_name}"


class Book(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	working_number = models.CharField(max_length=12, validators=[validate_underscore, validate_digits_after_underscore, validate_alpha_before_underscore, validate_two_letters])
	description = RichTextField(blank=True)
	comparible = models.URLField(max_length=200, blank=True)
	co_author_name = models.ManyToManyField(Author, related_name='co_author')
	co_author_instructions = RichTextField(blank=True)
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

	def delete(self, *args, **kwargs):
		if self.cover:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover.name))

		super(Book, self).delete(*args, **kwargs)

	def save(self):
		# opening the uploaded image
		im = Image.open(self.cover)

		output = BytesIO()

		# resize/modify the image
		# im = im.resize((100, 100))

		# after modifications, save it to the output
		try:
			im.save(output, format='JPEG', quality=30)
			output.seek(0)
			self.cover = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.cover.name.split('.')[0], 'image/jpeg', os.sys.getsizeof(output), None)
		except Exception:
			pass

		# output.seek(0)

		# change the imagefield value to be the newly modifed image value
		# self.cover = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.cover.name.split('.')[0], 'image/jpeg', os.sys.getsizeof(output), None)

		super(Book, self).save()


# # if the book's cover is changed, remove the old one - optimization
# @receiver(models.signals.pre_save, sender=Book)
# def auto_delete_file_on_change(sender, instance, **kwargs):
# 	if not instance.pk:
# 		return False

# 	try:
# 		old_file = sender.objects.get(pk=instance.pk).cover
# 	except sender.DoesNotExist:
# 		return False

# 	if old_file:
# 		new_file = instance.cover
# 		if not old_file == new_file:
# 			if os.path.isfile(old_file.path):
# 				os.remove(old_file.path)


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
	description = forms.CharField(widget=CKEditorWidget(), required=False)
	co_author_instructions = forms.CharField(widget=CKEditorWidget(), required=False)

	class Meta:
		model = Book
		fields = '__all__'
		# labels = {
		# 	'working_number': _('Working No'),
		# }
		# widgets = {
		# 	'author': Select2MultipleWidget,
		# 	'co_author_name': Select2MultipleWidget
		# }
