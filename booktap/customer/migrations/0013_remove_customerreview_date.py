# Generated by Django 2.2.5 on 2019-11-14 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customerreview_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerreview',
            name='date',
        ),
    ]
