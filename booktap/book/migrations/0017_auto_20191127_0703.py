# Generated by Django 2.2.5 on 2019-11-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_ebook_book_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='book_rated',
            field=models.FloatField(),
        ),
    ]