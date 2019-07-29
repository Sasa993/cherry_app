from django.db import models


class EBook(models.Model):
	name = models.CharField(max_length=50, default='E-Book', editable=False)
	title = models.CharField(max_length=100)
	source_file = models.FileField()
	epub_file = models.FileField()
	mobi_file = models.FileField()
	cover_file = models.FileField()

	def __str__(self):
		return f"{self.title}"

class Book5x8(models.Model):
	name = models.CharField(max_length=50, default='5x8 Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()

class BookA5Hardcover(models.Model):
	name = models.CharField(max_length=50, default='A5 Hardcover Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

class Book115x18Fnsku(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 FNSKU Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

class Book115x18Isbn(models.Model):
	name = models.CharField(max_length=50, default='11,5x18 ISBN Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

class Book125x19Hardcover(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 Hardcover Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

class Book125x19Fnsku(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 FNSKU Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()

class Book125x19Isbn(models.Model):
	name = models.CharField(max_length=50, default='12,5x19 ISBN Book', editable=False)
	title = models.CharField(max_length=100)
	cover_pdf_file = models.FileField()
	cover_psd_file = models.FileField()
	pdf_file = models.FileField()
	indesign_file = models.FileField()
	pdf_old_version_file = models.FileField()
	barcode_file = models.FileField()
	cover_interiour_pdf = models.FileField()
	cover_interiour_psd = models.FileField()