# Generated by Django 2.2.5 on 2019-10-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0013_auto_20191022_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signin',
            options={},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'default_permissions': ('change', 'add', 'delete', 'view')},
        ),
    ]