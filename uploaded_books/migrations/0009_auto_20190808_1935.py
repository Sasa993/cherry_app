# Generated by Django 2.2 on 2019-08-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_books', '0008_auto_20190808_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='source_file',
            field=models.FileField(upload_to='E-Book'),
        ),
    ]
