from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from uploaded_books.forms import (
	EBookForm, Book5x8Form, BookA5HardcoverForm, Book115x18FnskuForm, Book115x18IsbnForm, Book125x19HardcoverForm, Book125x19FnskuForm, Book125x19IsbnForm)
from uploaded_books.models import (EBook, Book5x8, Book125x19Isbn)
from itertools import chain


@login_required
def all_uploaded_books(request):
	all_ebooks = EBook.objects.all()
	all_books2 = Book5x8.objects.all()
	all_books3 = Book125x19Isbn.objects.all()

	neki_kurac = chain(all_ebooks, all_books2, all_books3)

	# context = {'all_ebooks': all_ebooks, 'all_books2': all_books2}
	context = {'neki_kurac': neki_kurac}

	return render(request, 'uploaded_books/all_uploaded_books.html', context)


@login_required
def upload_ebook(request):
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('uploaded_books:all_uploaded_books')
	else:
		form = EBookForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_ebook.html', context)

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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
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
			return redirect('uploaded_books:all_uploaded_books')
	else:
		form = Book125x19IsbnForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_125x19_isbn.html', context)


@login_required
def details_ebook(request, book_id):
	try:
		book = EBook.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'uploaded_books/details_ebook.html', context)
	except:
		raise Http404("No book!")
