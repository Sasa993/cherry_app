# Generated by Django 2.2 on 2019-08-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_books', '0021_auto_20190820_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book115x18fnsku',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='book115x18isbn',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='book125x19fnsku',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='book125x19hardcover',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='book125x19isbn',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='book5x8',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='booka5hardcover',
            name='book_ptr',
        ),
        migrations.RemoveField(
            model_name='ebook',
            name='book_ptr',
        ),
        migrations.AddField(
            model_name='book115x18fnsku',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book115x18isbn',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book125x19fnsku',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book125x19hardcover',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book125x19isbn',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book5x8',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booka5hardcover',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ebook',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
