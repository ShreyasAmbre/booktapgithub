# Generated by Django 2.2.5 on 2019-10-23 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0018_signin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='username',
        ),
    ]
