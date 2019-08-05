from django import forms
from django.utils.translation import ugettext_lazy as _
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)


class EBookForm(forms.ModelForm):
	class Meta:
		model = EBook
		exclude = ('name',)
		labels = {
			'source_file': _('Source File'),
			'epub_file': _('EPUB File'),
			'mobi_file': _('MOBI File'),
			'cover_file': _('Cover File'),
		}


class Book5x8Form(forms.ModelForm):
	class Meta:
		model = Book5x8
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
		}


class BookA5HardcoverForm(forms.ModelForm):
	class Meta:
		model = BookA5Hardcover
		exclude = ('name',)


class Book115x18FnskuForm(forms.ModelForm):
	class Meta:
		model = Book115x18Fnsku
		exclude = ('name',)


class Book115x18IsbnForm(forms.ModelForm):
	class Meta:
		model = Book115x18Isbn
		exclude = ('name',)


class Book125x19HardcoverForm(forms.ModelForm):
	class Meta:
		model = Book125x19Hardcover
		exclude = ('name',)


class Book125x19FnskuForm(forms.ModelForm):
	class Meta:
		model = Book125x19Fnsku
		exclude = ('name',)


class Book125x19IsbnForm(forms.ModelForm):
	class Meta:
		model = Book125x19Isbn
		exclude = ('name',)
