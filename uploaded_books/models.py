from django.db import models
from django.conf import settings
from books.models import Book
import os


class EBook(Book):
	name = models.CharField(max_length=50, default='E-Book', editable=False)
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


class Book5x8(Book):
	name = models.CharField(max_length=50, default='5x8 Book', editable=False)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()

	def __str__(self):
		return f"{self.title}"

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		super(Book5x8, self).delete(*args, **kwargs)


class BookA5Hardcover(Book):
	name = models.CharField(max_length=50, default='A5 Hardcover Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(BookA5Hardcover, self).delete(*args, **kwargs)


class Book115x18Fnsku(Book):
	name = models.CharField(max_length=50, default='11,5x18 FNSKU Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(Book115x18Fnsku, self).delete(*args, **kwargs)


class Book115x18Isbn(Book):
	name = models.CharField(max_length=50, default='11,5x18 ISBN Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(Book115x18Isbn, self).delete(*args, **kwargs)


class Book125x19Hardcover(Book):
	name = models.CharField(max_length=50, default='12,5x19 Hardcover Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(Book125x19Hardcover, self).delete(*args, **kwargs)


class Book125x19Fnsku(Book):
	name = models.CharField(max_length=50, default='12,5x19 FNSKU Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(Book125x19Fnsku, self).delete(*args, **kwargs)


class Book125x19Isbn(Book):
	name = models.CharField(max_length=50, default='12,5x19 ISBN Book', editable=False)
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

	# overriding the default "delete" method in order to delete all the uploaded files of the certain book
	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_psd_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.indesign_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.pdf_old_version_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.barcode_file.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_pdf.name))
		os.remove(os.path.join(settings.MEDIA_ROOT, self.cover_interiour_psd.name))
		super(Book125x19Isbn, self).delete(*args, **kwargs)
