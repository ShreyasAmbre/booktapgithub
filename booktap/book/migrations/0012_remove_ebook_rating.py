# Generated by Django 2.2.5 on 2019-11-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_ebook_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='rating',
        ),
    ]