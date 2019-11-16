# Generated by Django 2.2.5 on 2019-10-10 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_suppliersrecord'),
        ('customer', '0003_customerorders_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorders',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='supplier.SuppliersDetail'),
            preserve_default=False,
        ),
    ]
