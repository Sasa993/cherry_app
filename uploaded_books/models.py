from django.db import models
from django.conf import settings
# from books.models import Book
import os


class EBook(models.Model):
	name = models.CharField(max_length=50, default='E-Book', editable=False)
	# source_file = models.FileField(blank=True, default='no-file/no-file.png')
	source_file = models.FileField(blank=True)
	epub_file = models.FileField(blank=True)
	mobi_file = models.FileField(blank=True)
	cover_file = models.FileField(blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
	modified_at = models.DateTimeField(auto_now=True, blank=True)
	# book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f"{self.name}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.source_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.source_file.name))
		if self.epub_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.epub_file.name))
		if self.mobi_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.mobi_file.name))
		if self.cover_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_file.name))
		super(EBook, self).delete(*args, **kwargs)


class Book5x8(models.Model):
	name = models.CharField(max_length=50, default='5x8 Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))

		super(Book5x8, self).delete(*args, **kwargs)


class BookA5Hardcover(models.Model):
	name = models.CharField(max_length=50, default='A5 Hardcover Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(BookA5Hardcover, self).delete(*args, **kwargs)


class Book115x18Fnsku(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 FNSKU Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(Book115x18Fnsku, self).delete(*args, **kwargs)


class Book115x18Isbn(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 ISBN Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(Book115x18Isbn, self).delete(*args, **kwargs)


class Book125x19Hardcover(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 Hardcover Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(Book125x19Hardcover, self).delete(*args, **kwargs)


class Book125x19Fnsku(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 FNSKU Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(Book125x19Fnsku, self).delete(*args, **kwargs)


class Book125x19Isbn(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 ISBN Book', editable=False)
	cover_pdf_file = models.FileField(blank=True)
	cover_psd_file = models.FileField(blank=True)
	pdf_file = models.FileField(blank=True)
	indesign_file = models.FileField(blank=True)
	pdf_old_version_file = models.FileField(blank=True)
	barcode_file = models.FileField(blank=True)
	cover_interiour_pdf = models.FileField(blank=True)
	cover_interiour_psd = models.FileField(blank=True)

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		if self.cover_pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		if self.cover_psd_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		if self.pdf_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		if self.indesign_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		if self.pdf_old_version_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		if self.barcode_file:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		if self.cover_interiour_pdf:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		if self.cover_interiour_psd:
			os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))

		super(Book125x19Isbn, self).delete(*args, **kwargs)
