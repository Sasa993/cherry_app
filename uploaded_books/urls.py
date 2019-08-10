from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'uploaded_books'
urlpatterns = [
    # path('', views.all_uploaded_books, name='all_uploaded_books'),
    path('upload_ebook/', views.upload_ebook, name='upload_ebook'),
    path('choose_regular_book/', views.choose_regular_book, name='choose_regular_book'),
    path('choose_regular_book/upload_5x8/', views.upload_5x8, name='upload_5x8'),
    path('choose_regular_book/upload_a5_hardcover/', views.upload_a5_hardcover, name='upload_a5_hardcover'),
    path('choose_regular_book/upload_115x18_fnsku/', views.upload_115x18_fnsku, name='upload_115x18_fnsku'),
    path('choose_regular_book/upload_115x18_isbn/', views.upload_115x18_isbn, name='upload_115x18_isbn'),
    path('choose_regular_book/upload_125x19_hardcover', views.upload_125x19_hardcover, name='upload_125x19_hardcover'),
    path('choose_regular_book/upload_125x19_fnsku', views.upload_125x19_fnsku, name='upload_125x19_fnsku'),
    path('choose_regular_book/upload_125x19_isbn', views.upload_125x19_isbn, name='upload_125x19_isbn'),

    path('E-Book/<int:book_id>/', views.details_ebook, name='details_ebook'),
    path('E-Book/<int:book_id>/edit/', views.edit_ebook, name='edit_ebook'),
    path('E-Book/<int:book_id>/delete/', views.delete_ebook, name='delete_ebook'),
    path('E-Book/<int:book_id>/zip_whole_ebook/', views.zip_whole_ebook, name='zip_whole_ebook'),
    path('E-Book/<int:book_id>/zip_single_ebook/<str:ebook_type>', views.zip_single_ebook, name='zip_single_ebook'),

    path('5x8 Book/<int:book_id>/', views.details_5x8, name='details_5x8'),
    path('5x8 Book/<int:book_id>/edit/', views.edit_5x8, name='edit_5x8'),
    path('5x8 Book/<int:book_id>/delete/', views.delete_5x8, name='delete_5x8'),
    path('5x8 Book/<int:book_id>/zip_whole_5x8/', views.zip_whole_5x8, name='zip_whole_5x8'),
    path('5x8 Book/<int:book_id>/zip_single_5x8/<str:ebook_type>', views.zip_single_5x8, name='zip_single_5x8'),

    path('A5 Hardcover Book/<int:book_id>/', views.details_a5_hardcover, name='details_a5_hardcover'),
    path('A5 Hardcover Book/<int:book_id>/edit/', views.edit_a5_hardcover, name='edit_a5_hardcover'),
    path('A5 Hardcover Book/<int:book_id>/delete/', views.delete_a5_hardcover, name='delete_a5_hardcover'),
    path('A5 Hardcover Book/<int:book_id>/zip_whole_a5_hardcover/', views.zip_whole_a5_hardcover, name='zip_whole_a5_hardcover'),
    path('A5 Hardcover Book/<int:book_id>/zip_single_a5_hardcover/<str:ebook_type>', views.zip_single_a5_hardcover, name='zip_single_a5_hardcover'),

    path('11,5x18 FNSKU Book/<int:book_id>/', views.details_115x18_fnsku, name='details_115x18_fnsku'),
    path('11,5x18 FNSKU Book/<int:book_id>/edit/', views.edit_115x18_fnsku, name='edit_115x18_fnsku'),
    path('11,5x18 FNSKU Book/<int:book_id>/delete/', views.delete_115x18_fnsku, name='delete_115x18_fnsku'),
    path('11,5x18 FNSKU Book/<int:book_id>/zip_whole_115x18_fnsku/', views.zip_whole_115x18_fnsku, name='zip_whole_115x18_fnsku'),
    path('11,5x18 FNSKU Book/<int:book_id>/zip_single_115x18_fnsku/<str:ebook_type>', views.zip_single_115x18_fnsku, name='zip_single_115x18_fnsku'),

    path('11,5x18 ISBN Book/<int:book_id>/', views.details_115x18_isbn, name='details_115x18_isbn'),
    path('11,5x18 ISBN Book/<int:book_id>/edit/', views.edit_115x18_isbn, name='edit_115x18_isbn'),
    path('11,5x18 ISBN Book/<int:book_id>/delete/', views.delete_115x18_isbn, name='delete_115x18_isbn'),
    path('11,5x18 ISBN Book/<int:book_id>/zip_whole_115x18_isbn/', views.zip_whole_115x18_isbn, name='zip_whole_115x18_isbn'),
    path('11,5x18 ISBN Book/<int:book_id>/zip_single_115x18_isbn/<str:ebook_type>', views.zip_single_115x18_isbn, name='zip_single_115x18_isbn'),

    path('12,5x19 Hardcover Book/<int:book_id>/', views.details_125x19_hardcover, name='details_125x19_hardcover'),
    path('12,5x19 Hardcover Book/<int:book_id>/edit/', views.edit_125x19_hardcover, name='edit_125x19_hardcover'),
    path('12,5x19 Hardcover Book/<int:book_id>/delete/', views.delete_125x19_hardcover, name='delete_125x19_hardcover'),
    path('12,5x19 Hardcover Book/<int:book_id>/zip_whole_125x19_hardcover/', views.zip_whole_125x19_hardcover, name='zip_whole_125x19_hardcover'),
    path('12,5x19 Hardcover Book/<int:book_id>/zip_single_125x19_hardcover/<str:ebook_type>', views.zip_single_125x19_hardcover, name='zip_single_125x19_hardcover'),

    path('12,5x19 FNSKU Book/<int:book_id>/', views.details_125x19_fnsku, name='details_125x19_fnsku'),
    path('12,5x19 FNSKU Book/<int:book_id>/edit/', views.edit_125x19_fnsku, name='edit_125x19_fnsku'),
    path('12,5x19 FNSKU Book/<int:book_id>/delete/', views.delete_125x19_fnsku, name='delete_125x19_fnsku'),
    path('12,5x19 FNSKU Book/<int:book_id>/zip_whole_125x19_fnsku/', views.zip_whole_125x19_fnsku, name='zip_whole_125x19_fnsku'),
    path('12,5x19 FNSKU Book/<int:book_id>/zip_single_125x19_fnsku/<str:ebook_type>', views.zip_single_125x19_fnsku, name='zip_single_125x19_fnsku'),

    path('12,5x19 ISBN Book/<int:book_id>/', views.details_125x19_isbn, name='details_125x19_isbn'),
    path('12,5x19 ISBN Book/<int:book_id>/edit/', views.edit_125x19_isbn, name='edit_125x19_isbn'),
    path('12,5x19 ISBN Book/<int:book_id>/delete/', views.delete_125x19_isbn, name='delete_125x19_isbn'),
    path('12,5x19 ISBN Book/<int:book_id>/zip_whole_125x19_isbn/', views.zip_whole_125x19_isbn, name='zip_whole_125x19_isbn'),
    path('12,5x19 ISBN Book/<int:book_id>/zip_single_125x19_isbn/<str:ebook_type>', views.zip_single_125x19_isbn, name='zip_single_125x19_isbn'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
