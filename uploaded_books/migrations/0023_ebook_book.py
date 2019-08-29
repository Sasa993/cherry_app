# Generated by Django 2.2 on 2019-08-27 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0035_remove_book_ebook'),
        ('uploaded_books', '0022_auto_20190827_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
            preserve_default=False,
        ),
    ]