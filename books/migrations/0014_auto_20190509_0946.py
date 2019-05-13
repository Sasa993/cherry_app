# Generated by Django 2.2 on 2019-05-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20190509_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='co_author_email',
        ),
        migrations.AddField(
            model_name='book',
            name='co_author_email',
            field=models.ManyToManyField(related_name='co_author_email', to='books.Author'),
        ),
    ]