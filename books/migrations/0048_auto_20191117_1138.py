# Generated by Django 2.2 on 2019-11-17 10:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0047_auto_20191007_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]