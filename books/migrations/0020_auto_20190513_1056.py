# Generated by Django 2.2 on 2019-05-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20190513_0854'),
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
