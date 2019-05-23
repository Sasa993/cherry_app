from django.shortcuts import render, redirect
from django.http import Http404
from .models import (Author, Book, BookForm,
					 BookRequest)
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
import pdb

from django.dispatch import receiver, Signal

book_request = Signal(providing_args=['authors', 'requested_book'])

def index(request):

	return render(request, 'books/index.html', {})


def dashboard(request):
	# using order_by to make sure that the last added book shows as a first book
	all_books = Book.objects.all().order_by('-id')
	paginator = Paginator(all_books, 8)

	page = request.GET.get('page')
	books = paginator.get_page(page)
	context = {'books': books}

	return render(request, 'books/dashboard.html', context)


def details_books(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'books/details_books.html', context)
	except:
		raise Http404("Ne postoji ta knjiga!")


def enter_new_book(request):
	if (request.method == 'POST'):
		form = BookForm(request.POST, request.FILES)
		if (form.is_valid()):
			f = form.save()
			requested_book = BookRequest.objects.create(book=f)
			book_request.send(sender=Book, authors=form.cleaned_data['author'], requested_book = requested_book.pk)
			if ('save_and_add_another' in request.POST):
				return redirect('dashboard:enter_new_book')
			else:
				return redirect('dashboard:dashboard')
	else:
		form = BookForm()

	context = {'form': form}

	return render(request, 'books/enter_new_book.html', context)

@receiver(book_request)
def send_request_to_authors(sender, **kwargs):
	authors_mail = [x for x in kwargs['authors'].all().values_list('email', flat=True)]

	message = """You have been requested for a book creating. Please visit this link for more details:
	http://localhost:8000/dashboard/book-request/""" + str(kwargs['requested_book'])
	email = EmailMessage('Subject', message, to=authors_mail)
	email.send()

def edit_books(request, book_id):
	book = Book.objects.get(pk=book_id)
	if (request.method == 'POST'):
		form = BookForm(request.POST, request.FILES, instance=book)
		if(form.is_valid()):
			form.save()
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = BookForm(instance=book)

	context = {'book': book, 'form': form}

	return render(request, 'books/edit_books.html', context)

def book_requests(request, request_book_id):
	context = {}
	requested_book = BookRequest.objects.get(id=request_book_id)
	if request.method == 'POST':
		print("you did this")
	else:
		if request.user.email in requested_book.authors_accepted.all().values_list('email', flat=True):
			context["data"] = "decided"
		else:
			context["data"] = requested_book.book.title

	return render(request, 'books/book_request.html', context)

# getting AJAX's data and using it to query our DB
def load_emails(request):
	author_id = request.GET.getlist('authorId[]')
	# print(author_id)
	mails = Author.objects.filter(pk__in=author_id)

	return render(request, 'includes/displaying_emails_using_ajax.html', {'mails': mails})
