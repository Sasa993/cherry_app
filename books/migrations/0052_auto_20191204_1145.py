# Generated by Django 2.2 on 2019-12-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0051_auto_20191204_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploaded_books.EBook'),
        ),
    ]
