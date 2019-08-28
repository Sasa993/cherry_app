# Generated by Django 2.2 on 2019-08-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0036_book_ebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploaded_books.EBook'),
        ),
    ]
