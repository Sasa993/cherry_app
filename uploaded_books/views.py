from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
import json as simplejson
from django.db.models.functions import Lower
from uploaded_books.forms import (
	EBookForm, Book5x8Form, BookA5HardcoverForm, Book115x18FnskuForm, Book115x18IsbnForm, Book125x19HardcoverForm, Book125x19FnskuForm, Book125x19IsbnForm)
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)
from books.models import Book, BookForm
# from itertools import chain
# import operator
import zipfile


@login_required
def all_uploaded_books(request):
	sort_order = ""

	if request.GET:
		found_books = None
		if ("red" in request.GET) and request.GET["red"].strip():
			sort_order = request.GET["red"]

			if sort_order == "-title":
				all_books2 = Book.objects.all().extra(select={'lower_name': f'lower(title)'}).order_by('-lower_name')
			elif sort_order == "title":
				all_books2 = Book.objects.all().extra(select={'lower_name': f'lower({sort_order})'}).order_by('lower_name')
			else:
				all_books2 = Book.objects.all().order_by(sort_order)

			paginator = Paginator(all_books2, 11)
			page = request.GET.get('page')
			all_books = paginator.get_page(page)
		else:
			all_books2 = Book.objects.all().order_by("uploaded_at")
			paginator = Paginator(all_books2, 11)
			page = request.GET.get('page')
			all_books = paginator.get_page(page)
	else:
		all_books2 = Book.objects.all().order_by("uploaded_at")
		paginator = Paginator(all_books2, 11)
		page = request.GET.get('page')
		all_books = paginator.get_page(page)

	context = {"all_books": all_books}
	return render(request, 'uploaded_books/all_uploaded_books.html', context)


# E-Book
@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_ebook(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.ebook = EBook.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = EBookForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_ebook.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_ebook(request, main_book_id, book_id):
	book = EBook.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_ebook', args=[main_book_id, book_id]))
	else:
		form = EBookForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_ebook.html', context)


@login_required
def details_ebook(request, main_book_id, book_id):
	try:
		book = EBook.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_ebook.html', context)
	except Exception:
		raise Http404("We can not find that E-Book in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_ebook(request, book_id):
	book = EBook.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_ebook(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = EBook.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.source_file:
		zf.write(book.source_file.path, f'{book.source_file}')
	if book.epub_file:
		zf.write(book.epub_file.path, f'{book.epub_file}')
	if book.mobi_file:
		zf.write(book.mobi_file.path, f'{book.mobi_file}')
	if book.cover_file:
		zf.write(book.cover_file.path, f'{book.cover_file}')

	response['Content-Disposition'] = f'attachment; filename=EBook-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_ebook(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = EBook.objects.get(pk=book_id)

	if ebook_type == 'Source':
		zf.write(book.source_file.path, f'{book.source_file}')
	elif ebook_type == 'EPUB':
		zf.write(book.epub_file.path, f'{book.epub_file}')
	elif ebook_type == 'MOBI':
		zf.write(book.mobi_file.path, f'{book.mobi_file}')
	else:
		zf.write(book.cover_file.path, f'{book.cover_file}')

	response['Content-Disposition'] = f'attachment; filename=EBook-{ebook_type} File.zip'

	return response


# regular_books
@login_required
def choose_regular_book(request):

	return render(request, 'uploaded_books/choose_regular_book.html', {})


# 5x8 Book
@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_5x8(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book5x8Form(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book5x8 = Book5x8.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book5x8Form()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_5x8.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_5x8(request, main_book_id, book_id):
	book = Book5x8.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book5x8Form(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_5x8', args=[main_book_id, book_id]))
	else:
		form = Book5x8Form(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_5x8.html', context)


@login_required
def details_5x8(request, main_book_id, book_id):
	try:
		book = Book5x8.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_5x8.html', context)
	except Exception:
		raise Http404("We can not find that Book 5x8 in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_5x8(request, book_id):
	book = Book5x8.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_5x8(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book5x8.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')

	response['Content-Disposition'] = f'attachment; filename=Book5x8-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_5x8(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book5x8.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	else:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')

	response['Content-Disposition'] = f'attachment; filename=Book5x8-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_a5_hardcover(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = BookA5HardcoverForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_A5_hardcover = BookA5Hardcover.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = BookA5HardcoverForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_a5_hardcover.html', context)


@login_required
def details_a5_hardcover(request, main_book_id, book_id):
	try:
		book = BookA5Hardcover.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_a5_hardcover.html', context)
	except Exception:
		raise Http404("We can not find that Book A5 Hardcover in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_a5_hardcover(request, main_book_id, book_id):
	book = BookA5Hardcover.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = BookA5HardcoverForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_a5_hardcover', args=[main_book_id, book_id]))
	else:
		form = BookA5HardcoverForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_a5_hardcover.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_a5_hardcover(request, book_id):
	book = BookA5Hardcover.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_a5_hardcover(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = BookA5Hardcover.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=BookA5Hardcover-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_a5_hardcover(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = BookA5Hardcover.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=BookA5Hardcover-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_115x18_fnsku(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book115x18FnskuForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_115x18_fnsku = Book115x18Fnsku.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book115x18FnskuForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_115x18_fnsku.html', context)


@login_required
def details_115x18_fnsku(request, main_book_id, book_id):
	try:
		book = Book115x18Fnsku.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_115x18_fnsku.html', context)
	except Exception:
		raise Http404("We can not find that Book 115x18 FNSKU in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_115x18_fnsku(request, main_book_id, book_id):
	book = Book115x18Fnsku.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book115x18FnskuForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_115x18_fnsku', args=[main_book_id, book_id]))
	else:
		form = Book115x18FnskuForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_115x18_fnsku.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_115x18_fnsku(request, book_id):
	book = Book115x18Fnsku.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_115x18_fnsku(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book115x18Fnsku.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book115x18Fnsku-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_115x18_fnsku(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book115x18Fnsku.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book115x18Fnsku-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_115x18_isbn(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book115x18IsbnForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_115x18_isbn = Book115x18Isbn.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book115x18IsbnForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_115x18_isbn.html', context)


@login_required
def details_115x18_isbn(request, main_book_id, book_id):
	try:
		book = Book115x18Isbn.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_115x18_isbn.html', context)
	except Exception:
		raise Http404("We can not find that Book 115x18 ISBN in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_115x18_isbn(request, main_book_id, book_id):
	book = Book115x18Isbn.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book115x18IsbnForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_115x18_isbn', args=[main_book_id, book_id]))
	else:
		form = Book115x18IsbnForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_115x18_isbn.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_115x18_isbn(request, book_id):
	book = Book115x18Isbn.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_115x18_isbn(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book115x18Isbn.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book115x18Isbn-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_115x18_isbn(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book115x18Isbn.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book115x18Isbn-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_125x19_hardcover(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book125x19HardcoverForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_125x19_hardcover = Book125x19Hardcover.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book125x19HardcoverForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_125x19_hardcover.html', context)


@login_required
def details_125x19_hardcover(request, main_book_id, book_id):
	try:
		book = Book125x19Hardcover.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_125x19_hardcover.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 Hardcover in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_125x19_hardcover(request, main_book_id, book_id):
	book = Book125x19Hardcover.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book125x19HardcoverForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_125x19_hardcover', args=[main_book_id, book_id]))
	else:
		form = Book125x19HardcoverForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_125x19_hardcover.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_125x19_hardcover(request, book_id):
	book = Book125x19Hardcover.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_125x19_hardcover(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Hardcover.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19KDP-TB-ISBN-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_125x19_hardcover(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Hardcover.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19KDP-TB-ISBN-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_125x19_fnsku(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book125x19FnskuForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_125x19_fnsku = Book125x19Fnsku.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book125x19FnskuForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_125x19_fnsku.html', context)


@login_required
def details_125x19_fnsku(request, main_book_id, book_id):
	try:
		book = Book125x19Fnsku.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_125x19_fnsku.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 FNSKU in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_125x19_fnsku(request, main_book_id, book_id):
	book = Book125x19Fnsku.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book125x19FnskuForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_125x19_fnsku', args=[main_book_id, book_id]))
	else:
		form = Book125x19FnskuForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_125x19_fnsku.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_125x19_fnsku(request, book_id):
	book = Book125x19Fnsku.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_125x19_fnsku(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Fnsku.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19Fnsku-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_125x19_fnsku(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Fnsku.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19Fnsku-{ebook_type} File.zip'

	return response


@login_required
@user_passes_test(lambda u: u.is_superuser)
def upload_125x19_isbn(request, book_id):
	main_book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = Book125x19IsbnForm(request.POST, request.FILES)
		form_main_book = BookForm(instance=main_book)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.save()
			form3 = form_main_book.save(commit=False)
			form3.book_125x19_isbn = Book125x19Isbn.objects.get(pk=form2.pk)
			form3.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = Book125x19IsbnForm()

	context = {'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/upload_125x19_isbn.html', context)


@login_required
def details_125x19_isbn(request, main_book_id, book_id):
	try:
		book = Book125x19Isbn.objects.get(pk=book_id)
		main_book = Book.objects.get(pk=main_book_id)
		context = {'book': book, 'main_book': main_book}
		return render(request, 'uploaded_books/details/details_125x19_isbn.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 ISBN in our database.")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_125x19_isbn(request, main_book_id, book_id):
	book = Book125x19Isbn.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if request.method == 'POST':
		form = Book125x19IsbnForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_125x19_isbn', args=[main_book_id, book_id]))
	else:
		form = Book125x19IsbnForm(instance=book)

	context = {'book': book, 'main_book': main_book, 'form': form}

	return render(request, 'uploaded_books/edit_125x19_isbn.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_125x19_isbn(request, book_id):
	book = Book125x19Isbn.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_125x19_isbn(request, main_book_id, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Isbn.objects.get(pk=book_id)
	main_book = Book.objects.get(pk=main_book_id)
	if book.cover_pdf_file:
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	if book.cover_psd_file:
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	if book.pdf_file:
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	if book.indesign_file:
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	if book.pdf_old_version_file:
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	if book.barcode_file:
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	if book.cover_interiour_pdf:
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	if book.cover_interiour_psd:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19Isbn-[{main_book.working_number}] {main_book.title}.zip'

	return response


@login_required
def zip_single_125x19_isbn(request, book_id, ebook_type):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = Book125x19Isbn.objects.get(pk=book_id)

	if ebook_type == 'Cover PDF':
		zf.write(book.cover_pdf_file.path, f'{book.cover_pdf_file}')
	elif ebook_type == 'Cover PSD':
		zf.write(book.cover_psd_file.path, f'{book.cover_psd_file}')
	elif ebook_type == 'PDF':
		zf.write(book.pdf_file.path, f'{book.pdf_file}')
	elif ebook_type == 'InDesign':
		zf.write(book.indesign_file.path, f'{book.indesign_file}')
	elif ebook_type == 'PDF Old Version':
		zf.write(book.pdf_old_version_file.path, f'{book.pdf_old_version_file}')
	elif ebook_type == 'Barcode':
		zf.write(book.barcode_file.path, f'{book.barcode_file}')
	elif ebook_type == 'Cover Interiour PDF':
		zf.write(book.cover_interiour_pdf.path, f'{book.cover_interiour_pdf}')
	else:
		zf.write(book.cover_interiour_psd.path, f'{book.cover_interiour_psd}')

	response['Content-Disposition'] = f'attachment; filename=Book125x19Isbn-{ebook_type} File.zip'

	return response
