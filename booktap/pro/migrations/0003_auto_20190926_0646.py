# Generated by Django 2.2.5 on 2019-09-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_auto_20190926_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='agree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='signin',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='signin',
            name='is_end_user',
            field=models.BooleanField(default=False),
        ),
    ]
