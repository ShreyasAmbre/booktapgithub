# Generated by Django 2.2.5 on 2019-10-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EBook',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='ebook',
            new_name='book',
        ),
    ]
