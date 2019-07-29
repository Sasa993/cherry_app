from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EBookForm
from .models import EBook


@login_required
def all_uploaded_books(request):
	all_ebooks = EBook.objects.all().order_by('-id')
	context = {'all_ebooks': all_ebooks}

	return render(request, 'uploaded_books/all_uploaded_books.html', context)


@login_required
def upload_ebook(request):
	if request.method == 'POST':
		form = EBookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('uploaded_books:upload_ebook')
	else:
		form = EBookForm()

	context = {'form': form}

	return render(request, 'uploaded_books/upload_ebook.html', context)

#regular_books
@login_required
def choose_regular_book(request):

	return render(request, 'uploaded_books/choose_regular_book.html', {})

@login_required
def upload_5x8(request):

	return render(request, 'uploaded_books/upload_5x8.html', {})

@login_required
def upload_a5_hardcover(request):

	return render(request, 'uploaded_books/upload_a5_hardcover.html', {})

@login_required
def upload_115x18_fnsku(request):

	return render(request, 'uploaded_books/upload_115x18_fnsku.html', {})

@login_required
def upload_115x18_isbn(request):

	return render(request, 'uploaded_books/upload_115x18_isbn.html', {})

@login_required
def upload_125x19_hardcover(request):

	return render(request, 'uploaded_books/upload_125x19_hardcover.html', {})

@login_required
def upload_125x19_fnsku(request):

	return render(request, 'uploaded_books/upload_125x19_fnsku.html', {})

@login_required
def upload_125x19_isbn(request):

	return render(request, 'uploaded_books/upload_125x19_isbn.html', {})
