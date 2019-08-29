# Generated by Django 2.2 on 2019-08-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_books', '0022_auto_20190827_0816'),
        ('books', '0032_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ebook',
        ),
        migrations.AddField(
            model_name='book',
            name='ebook',
            field=models.ManyToManyField(blank=True, null=True, to='uploaded_books.EBook'),
        ),
    ]