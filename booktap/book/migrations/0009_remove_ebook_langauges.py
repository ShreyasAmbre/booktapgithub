# Generated by Django 2.2.5 on 2019-11-05 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20191105_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='langauges',
        ),
    ]