# Generated by Django 2.2 on 2019-08-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_books', '0023_ebook_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]