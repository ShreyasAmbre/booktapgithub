# Generated by Django 2.2.5 on 2019-10-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_ebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='book',
            field=models.FileField(upload_to='ebook'),
        ),
    ]