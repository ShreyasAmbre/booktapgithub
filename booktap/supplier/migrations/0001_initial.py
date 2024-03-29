# Generated by Django 2.2.5 on 2019-10-10 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pro', '0004_auto_20191009_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuppliersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('company_name', models.CharField(max_length=50)),
                ('bank_account', models.CharField(max_length=50)),
                ('account_name', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('upi_id', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Signin')),
            ],
        ),
    ]
