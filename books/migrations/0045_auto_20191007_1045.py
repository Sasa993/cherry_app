# Generated by Django 2.2 on 2019-10-07 08:45

import books.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0044_auto_20191007_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='working_number',
            field=models.CharField(max_length=12, validators=[books.validators.validate_underscore, books.validators.validate_digits_after_underscore]),
        ),
    ]
