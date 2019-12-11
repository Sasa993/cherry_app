from django.db.models.signals import pre_save
from django.dispatch import receiver
from books.models import Book
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn
)
import os


# if the book's cover is changed, remove the old one - optimization
@receiver(pre_save, sender=Book)
def auto_delete_file_on_change(sender, instance, **kwargs):
	if not instance.pk:
		return False

	try:
		old_file = sender.objects.get(pk=instance.pk).cover
	except sender.DoesNotExist:
		return False

	if old_file:
		new_file = instance.cover
		if not old_file == new_file:
			if os.path.isfile(old_file.path):
				os.remove(old_file.path)


# if any of the book types' files are changed/edited, remove the old ones - optimization
@receiver(pre_save, sender=EBook)
@receiver(pre_save, sender=Book5x8)
@receiver(pre_save, sender=BookA5Hardcover)
@receiver(pre_save, sender=Book115x18Fnsku)
@receiver(pre_save, sender=Book115x18Isbn)
@receiver(pre_save, sender=Book125x19Hardcover)
@receiver(pre_save, sender=Book125x19Fnsku)
@receiver(pre_save, sender=Book125x19Isbn)
def auto_delete_file_on_change_ebook(sender, instance, **kwargs):
	if sender == EBook:
		list_of_fields = ["source_file", "epub_file", "mobi_file", "cover_file"]
	elif sender == Book5x8:
		list_of_fields = ["cover_pdf_file", "cover_psd_file", "pdf_file", "indesign_file", "pdf_old_version_file", "barcode_file"]
	elif sender == BookA5Hardcover or sender == Book115x18Fnsku or sender == Book115x18Isbn or sender == Book125x19Hardcover or sender == Book125x19Fnsku or sender == Book125x19Isbn:
		list_of_fields = ["cover_pdf_file", "cover_psd_file", "pdf_file", "indesign_file", "pdf_old_version_file", "barcode_file", "cover_interiour_pdf", "cover_interiour_psd"]

	for field in range(len(list_of_fields)):
		try:
			old_file = getattr(sender.objects.get(pk=instance.pk), list_of_fields[field])
			if old_file:
				new_file = getattr(instance, list_of_fields[field])
				if not old_file == new_file:
					if os.path.isfile(old_file.path):
						os.remove(old_file.path)
		except sender.DoesNotExist:
			pass
