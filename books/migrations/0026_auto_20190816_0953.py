# Generated by Django 2.2 on 2019-08-16 07:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_remove_book_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Book')),
                ('name', models.CharField(default='E-Book', editable=False, max_length=50)),
                ('source_file', models.FileField(upload_to='')),
                ('epub_file', models.FileField(upload_to='')),
                ('mobi_file', models.FileField(upload_to='')),
                ('cover_file', models.FileField(upload_to='')),
            ],
            bases=('books.book',),
        ),
        migrations.AddField(
            model_name='book',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
