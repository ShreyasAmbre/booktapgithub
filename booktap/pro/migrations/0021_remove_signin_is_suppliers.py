# Generated by Django 2.2.5 on 2019-11-08 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0020_auto_20191105_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='is_suppliers',
        ),
    ]
