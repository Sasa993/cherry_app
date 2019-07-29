from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'uploaded_books'
urlpatterns = [
    path('', views.all_uploaded_books, name='all_uploaded_books'),
    path('upload_ebook/', views.upload_ebook, name='upload_ebook'),
    path('choose_regular_book/', views.choose_regular_book, name='choose_regular_book'),
    path('choose_regular_book/upload_5x8/', views.upload_5x8, name='upload_5x8' ),
    path('choose_regular_book/upload_a5_hardcover/', views.upload_a5_hardcover, name='upload_a5_hardcover'),
    path('choose_regular_book/upload_115x18_fnsku/', views.upload_115x18_fnsku, name='upload_115x18_fnsku'),
    path('choose_regular_book/upload_115x18_isbn/', views.upload_115x18_isbn, name='upload_115x18_isbn'),
    path('choose_regular_book/upload_125x19_hardcover', views.upload_125x19_hardcover, name='upload_125x19_hardcover'),
    path('choose_regular_book/upload_125x19_fnsku', views.upload_125x19_fnsku, name='upload_125x19_fnsku'),
    path('choose_regular_book/upload_125x19_isbn', views.upload_125x19_isbn, name='upload_125x19_isbn'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
