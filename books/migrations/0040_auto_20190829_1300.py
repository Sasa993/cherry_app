# Generated by Django 2.2 on 2019-08-29 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0039_auto_20190829_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_A5_Hardcover',
            new_name='book_A5_hardcover',
        ),
    ]
