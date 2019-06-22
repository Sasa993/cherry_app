from django.contrib import admin
from django.urls import path

from .views import email_main, email_success

app_name = "sendemail"

urlpatterns = [
    path('', email_main, name='email'),
    path('success/', email_success, name='success'),
]
