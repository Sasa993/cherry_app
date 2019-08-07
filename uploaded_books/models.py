from django.db import models
from django.conf import settings
import os


class EBook(models.Model):
	name = models.CharField(max_length=50, default='E-Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	source_file = models.FileField()
	epub_file = models.FileField()
	mobi_file = models.FileField()
	cover_file = models.FileField()

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.source_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.epub_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.mobi_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_file.name))
		super(EBook, self).delete(*args, **kwargs)


class Book5x8(models.Model):
	name = models.CharField(max_length=50, default='5x8 Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()

	def __str__(self):
		return f"{self.title}"


class BookA5Hardcover(models.Model):
	name = models.CharField(max_length=50, default='A5 Hardcover Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"


class Book115x18Fnsku(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 FNSKU Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"


class Book115x18Isbn(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 ISBN Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"


class Book125x19Hardcover(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 Hardcover Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"


class Book125x19Fnsku(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 FNSKU Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"


class Book125x19Isbn(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 ISBN Book', editable=False)
	title = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

	def __str__(self):
		return f"{self.title}"
