# Generated by Django 2.2 on 2019-08-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0035_remove_book_ebook'),
        ('uploaded_books', '0024_auto_20190827_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='book',
        ),
        migrations.AddField(
            model_name='ebook',
            name='book',
            field=models.ManyToManyField(related_name='main_book', to='books.Book'),
        ),
    ]