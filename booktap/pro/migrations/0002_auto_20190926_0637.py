# Generated by Django 2.2.5 on 2019-09-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='signin',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
