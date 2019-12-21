from django.urls import path
from . import views
from uploaded_books.views import all_uploaded_books, ajax_test

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'
urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('', all_uploaded_books, name='all_uploaded_books'),
    path('ajax/test', ajax_test, name='ajax_test'),
    path('<int:book_id>/', views.details_books, name='details_books'),
    path('<int:book_id>/edit/', views.edit_books, name='edit_books'),
    path('<int:book_id>/delete/', views.delete_books, name='delete_books'),
    path('enter_new_book', views.enter_new_book, name="enter_new_book"),
    path('ajax/load-emails', views.load_emails, name='ajax_load_emails'),
    path('book-request/<int:request_book_id>', views.book_requests, name='book-request'),
    path('book_search/', views.book_search, name='book_search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
