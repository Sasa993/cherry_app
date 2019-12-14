from django.shortcuts import render, redirect
from django.db.models import Q
from .models import (Author, Book, BookForm,
					BookRequest)
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver, Signal
import time

book_request = Signal(providing_args=['authors', 'requested_book'])


@login_required
def index(request):

	return render(request, 'books/index.html', {})


@login_required
def dashboard(request):
	# using order_by to make sure that the last added book shows as a first book
	all_books = Book.objects.all().order_by('-id')
	paginator = Paginator(all_books, 8)

	page = request.GET.get('page')
	books = paginator.get_page(page)
	context = {'books': books}

	return render(request, 'books/dashboard.html', context)


@login_required
def details_books(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
		context = {'book': book}
		return render(request, 'books/details_books.html', context)
	except Book.DoesNotExist:
		return render(request, 'errors/no_book_found.html', {'book_id': book_id})


@login_required
def enter_new_book(request):
	if (request.method == 'POST'):
		form = BookForm(request.POST, request.FILES)
		if (form.is_valid()):
			f = form.save()
			# commented to avoid the 500 server error in production
			# book_request.send(sender=Book, authors=form.cleaned_data['author'], requested_book=f.id)
			time.sleep(1)
			if ('save_and_add_another' in request.POST):
				return redirect('dashboard:enter_new_book')
			else:
				return redirect('dashboard:all_uploaded_books')
	else:
		form = BookForm()

	context = {'form': form}

	return render(request, 'books/enter_new_book.html', context)


@receiver(book_request)
def send_request_to_authors(sender, **kwargs):
	authors_mail = [x for x in kwargs['authors'].all().values_list('email', flat=True)]

	message = """You have been requested for a book creating. Please visit this link for more details:
	http://localhost:8000/dashboard/book-request/""" + str(kwargs['requested_book'])
	email = EmailMessage('Book request', message, to=authors_mail)
	email.send()


@login_required
def edit_books(request, book_id):
	book = Book.objects.get(pk=book_id)
	if (request.method == 'POST'):
		form = BookForm(request.POST, request.FILES, instance=book)
		if(form.is_valid()):
			form.save()
			time.sleep(1)
			return redirect(reverse('dashboard:details_books', args=[book_id]))
	else:
		form = BookForm(instance=book)

	context = {'book': book, 'form': form}

	return render(request, 'books/edit_books.html', context)


@login_required
def delete_books(request, book_id):
	book = Book.objects.get(pk=book_id)

	if Book.objects.get(pk=book_id).ebook:
		Book.objects.get(pk=book_id).ebook.delete()
	if Book.objects.get(pk=book_id).book5x8:
		Book.objects.get(pk=book_id).book5x8.delete()
	if Book.objects.get(pk=book_id).book_A5_hardcover:
		Book.objects.get(pk=book_id).book_A5_hardcover.delete()
	if Book.objects.get(pk=book_id).book_115x18_fnsku:
		Book.objects.get(pk=book_id).book_115x18_fnsku.delete()
	if Book.objects.get(pk=book_id).book_115x18_isbn:
		Book.objects.get(pk=book_id).book_115x18_isbn.delete()
	if Book.objects.get(pk=book_id).book_125x19_hardcover:
		Book.objects.get(pk=book_id).book_125x19_hardcover.delete()
	if Book.objects.get(pk=book_id).book_125x19_fnsku:
		Book.objects.get(pk=book_id).book_125x19_fnsku.delete()
	if Book.objects.get(pk=book_id).book_125x19_isbn:
		Book.objects.get(pk=book_id).book_125x19_isbn.delete()

	book.delete()
	# book2.delete()
	time.sleep(1)
	return redirect(reverse('dashboard:all_uploaded_books'))

# we need to change author model, this example is only for presenting
@login_required
def book_requests(request, request_book_id):
	context = {}
	book = Book.objects.get(id=request_book_id)
	if request.method == 'POST':
		if request.POST['decision'] == '1':
			author = Author.objects.filter(email=request.user.email)
			BookRequest.objects.create(book=book, authors_accepted=author[0], deadline=request.POST['deadline'], decision=request.POST['decision'])
		else:
			author = Author.objects.filter(email=request.user.email)
			BookRequest.objects.create(book=book, authors_accepted=author[0], decision=request.POST['decision'])
	else:
		requested_book = BookRequest.objects.filter(book=book).values_list('authors_accepted__email', flat=True)
		if request.user.email in [mail for mail in requested_book]:
			context["data"] = "decided"
		else:
			context["data"] = book.title
			context["desc"] = book.description
			context["id"] = request_book_id

	return render(request, 'books/book_request.html', context)


# getting AJAX's data and using it to query our DB
def load_emails(request):
	author_id = request.GET.getlist('authorId[]')
	# print(author_id)
	mails = Author.objects.filter(pk__in=author_id)

	return render(request, 'includes/displaying_emails_using_ajax.html', {'mails': mails})


@login_required
def handler404(request, exception, template_name="errors/error_404.html"):
	response = render(request, "errors/error_404.html")
	response.status_code = 404
	return response


@login_required
def book_search(request):

	query_string = ""

	if request.GET:

		found_books = None
		found_books2 = None
		if ("s_book" in request.GET) and request.GET["s_book"].strip():
			query_string = request.GET["s_book"]

			# querying through the "ModelMultipleChoiceField" fields and later uniting with found_books2 - so that we don't get duplicates in our search results, when there is more than 1 author or co_author
			search_for_multiple = found_books2 = Book.objects.filter(
				Q(author__name__icontains=query_string) | Q(author__last_name__icontains=query_string) | Q(co_author_name__name__icontains=query_string) | Q(co_author_name__last_name__icontains=query_string)
			)
			found_books2 = Book.objects.filter(
				Q(title__icontains=query_string) | Q(subtitle__icontains=query_string) | Q(working_number__icontains=query_string) | Q(description__icontains=query_string)
			)

			found_books2 = search_for_multiple.union(found_books2)
			paginator = Paginator(found_books2, 6)
			page = request.GET.get('page')
			found_books = paginator.get_page(page)
		else:
			# What if they selected the "completed" toggle but didn't enter a query string?
			# We still need found_tasks in a queryset so it can be "excluded" below.
			found_books2 = Book.objects.all()
			paginator = Paginator(found_books2, 6)
			page = request.GET.get('page')
			found_books = paginator.get_page(page)

		# if "inc_complete" in request.GET:
		# 	found_books = found_books.exclude(completed=True)

	else:
		found_books = None
		found_books2 = None

	context = {"query_string": query_string, "found_books2": found_books2, "found_books": found_books}
	return render(request, "books/search_books_results.html", context)
