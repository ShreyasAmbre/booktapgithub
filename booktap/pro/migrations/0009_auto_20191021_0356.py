# Generated by Django 2.2.5 on 2019-10-21 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0008_auto_20191011_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]