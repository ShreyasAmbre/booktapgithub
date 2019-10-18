# Generated by Django 2.2.5 on 2019-10-10 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0004_auto_20191009_1106'),
        ('book', '0003_book_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReviewRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Signin')),
            ],
        ),
    ]
