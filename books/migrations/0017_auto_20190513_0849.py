# Generated by Django 2.2 on 2019-05-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20190509_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='co_author_email',
        ),
        migrations.AddField(
            model_name='book',
            name='co_author_email',
            field=models.CharField(default=1.0, max_length=100),
            preserve_default=False,
        ),
    ]
