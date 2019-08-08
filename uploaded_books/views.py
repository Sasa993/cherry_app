from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from uploaded_books.forms import (
	EBookForm, Book5x8Form, BookA5HardcoverForm, Book115x18FnskuForm, Book115x18IsbnForm, Book125x19HardcoverForm, Book125x19FnskuForm, Book125x19IsbnForm)
from uploaded_books.models import (
	EBook, Book5x8, BookA5Hardcover, Book115x18Fnsku, Book115x18Isbn, Book125x19Hardcover, Book125x19Fnsku, Book125x19Isbn)
from itertools import chain
import operator

import zipfile


@login_required
def all_uploaded_books(request):
	all_ebooks = EBook.objects.all()
	all_books_5x8 = Book5x8.objects.all()
	all_books_a5hardcover = BookA5Hardcover.objects.all()
	all_books_115x18fnsku = Book115x18Fnsku.objects.all()
	all_books_115x18isbn = Book115x18Isbn.objects.all()
	all_books_125x19hardcover = Book125x19Hardcover.objects.all()
	all_books_125x19fnsku = Book125x19Fnsku.objects.all()
	all_books_125x19isbn = Book125x19Isbn.objects.all()

	every_fking_book = chain(all_ebooks, all_books_5x8, all_books_a5hardcover, all_books_115x18fnsku, all_books_115x18isbn, all_books_125x19hardcover, all_books_125x19fnsku, all_books_125x19isbn)
	every_fking_book = sorted(every_fking_book, key=operator.attrgetter('uploaded_at'), reverse=True)

	context = {'every_fking_book': every_fking_book}

	return render(request, 'uploaded_books/all_uploaded_books.html', context)


# e-book
@login_required
def upload_ebook(request):
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = EBookForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_ebook.html', context)


@login_required
def edit_ebook(request, book_id):
	book = EBook.objects.get(pk=book_id)
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			form.save()
			return redirect(reverse('uploaded_books:details_ebook', args=[book_id]))
	else:
		form = EBookForm(instance=book)

	context = {'book': book, 'form': form}

	return render(request, 'uploaded_books/edit_ebook.html', context)


@login_required
def delete_ebook(request, book_id):
	book = EBook.objects.get(pk=book_id)
	book.delete()
	return redirect(reverse('dashboard:all_uploaded_books'))


@login_required
def zip_whole_ebook(request, book_id):
	response = HttpResponse(content_type='application/zip')
	zf = zipfile.ZipFile(response, 'w')

	book = EBook.objects.get(pk=book_id)
	zf.write(book.source_file.path, f'{book.source_file}')
	zf.write(book.epub_file.path, f'{book.epub_file}')
	zf.write(book.mobi_file.path, f'{book.mobi_file}')
	zf.write(book.cover_file.path, f'{book.cover_file}')

	response['Content-Disposition'] = f'attachment; filename=EBook-{book.title}.zip'

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

	response['Content-Disposition'] = f'attachment; filename=EBook-{book.title}-{ebook_type} File.zip'

	return response


# regular_books
@login_required
def choose_regular_book(request):

	return render(request, 'uploaded_books/choose_regular_book.html', {})


@login_required
def upload_5x8(request):
	if request.method == 'POST':
		form = Book5x8Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book5x8Form()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_5x8.html', context)


@login_required
def upload_a5_hardcover(request):
	if request.method == 'POST':
		form = BookA5HardcoverForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = BookA5HardcoverForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_a5_hardcover.html', context)


@login_required
def upload_115x18_fnsku(request):
	if request.method == 'POST':
		form = Book115x18FnskuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book115x18FnskuForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_115x18_fnsku.html', context)


@login_required
def upload_115x18_isbn(request):
	if request.method == 'POST':
		form = Book115x18IsbnForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book115x18IsbnForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_115x18_isbn.html', context)


@login_required
def upload_125x19_hardcover(request):
	if request.method == 'POST':
		form = Book125x19HardcoverForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book125x19HardcoverForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_125x19_hardcover.html', context)


@login_required
def upload_125x19_fnsku(request):
	if request.method == 'POST':
		form = Book125x19FnskuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book125x19FnskuForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_125x19_fnsku.html', context)


@login_required
def upload_125x19_isbn(request):
	if request.method == 'POST':
		form = Book125x19IsbnForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard:all_uploaded_books')
	else:
		form = Book125x19IsbnForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_125x19_isbn.html', context)

# details
@login_required
def details_ebook(request, book_id):
	try:
		book = EBook.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_ebook.html', context)
	except Exception:
		raise Http404("We can not find that E-Book in our database.")


@login_required
def details_5x8(request, book_id):
	try:
		book = Book5x8.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_5x8.html', context)
	except Exception:
		raise Http404("We can not find that Book 5x8 in our database.")


@login_required
def details_a5_hardcover(request, book_id):
	try:
		book = BookA5Hardcover.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_a5_hardcover.html', context)
	except Exception:
		raise Http404("We can not find that Book A5 Hardcover in our database.")


@login_required
def details_115x18_fnsku(request, book_id):
	try:
		book = Book115x18Fnsku.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_115x18_fnsku.html', context)
	except Exception:
		raise Http404("We can not find that Book 115x18 FNSKU in our database.")


@login_required
def details_115x18_isbn(request, book_id):
	try:
		book = Book115x18Isbn.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_115x18_isbn.html', context)
	except Exception:
		raise Http404("We can not find that Book 115x18 ISBN in our database.")


@login_required
def details_125x19_hardcover(request, book_id):
	try:
		book = Book125x19Hardcover.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_125x19_hardcover.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 Hardcover in our database.")


@login_required
def details_125x19_fnsku(request, book_id):
	try:
		book = Book125x19Fnsku.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_125x19_fnsku.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 FNSKU in our database.")


@login_required
def details_125x19_isbn(request, book_id):
	try:
		book = Book125x19Isbn.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details/details_125x19_isbn.html', context)
	except Exception:
		raise Http404("We can not find that Book 125x19 ISBN in our database.")
