from django import forms
from django_select2.forms import Select2MultipleWidget
from books.models import Author, Book, BookForm
from django.utils.translation import ugettext_lazy as _
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)


class EBookForm(forms.ModelForm):
	author = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all(), required=False)
	co_author_name = forms.ModelMultipleChoiceField(widget=Select2MultipleWidget, queryset=Author.objects.all(), required=False)

	class Meta:
		model = EBook
		exclude = ('name',)
		labels = {
			'source_file': _('Source File'),
			'epub_file': _('EPUB File'),
			'mobi_file': _('MOBI File'),
			'cover_file': _('Cover File'),
			'working_number': _('Working No'),
		}


class Book5x8Form(EBookForm):
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
			'working_number': _('Working No'),
		}


class BookA5HardcoverForm(EBookForm):
	class Meta:
		model = BookA5Hardcover
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}


class Book115x18FnskuForm(EBookForm):
	class Meta:
		model = Book115x18Fnsku
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}


class Book115x18IsbnForm(EBookForm):
	class Meta:
		model = Book115x18Isbn
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}


class Book125x19HardcoverForm(EBookForm):
	class Meta:
		model = Book125x19Hardcover
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}


class Book125x19FnskuForm(EBookForm):
	class Meta:
		model = Book125x19Fnsku
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}


class Book125x19IsbnForm(EBookForm):
	class Meta:
		model = Book125x19Isbn
		exclude = ('name',)
		labels = {
			'cover_pdf_file': _('Cover PDF File'),
			'cover_psd_file': _('Cover PSD File'),
			'pdf_file': _('PDF File'),
			'indesign_file': _('InDesign File'),
			'pdf_old_version_file': _('PDF Old Version File'),
			'barcode_file': _('Barcode File'),
			'cover_interiour_pdf': _('Cover Interiour PDF'),
			'cover_interiour_psd': _('Cover Interiour PSD'),
			'working_number': _('Working No'),
		}
