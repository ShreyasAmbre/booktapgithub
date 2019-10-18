# Generated by Django 2.2.5 on 2019-10-12 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_suppliersrecord'),
        ('book', '0005_book_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='booksimages')),
                ('book', models.FileField(upload_to='book')),
                ('price', models.IntegerField()),
                ('edition', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('publication_name', models.CharField(max_length=50)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('features', models.BooleanField(default=False)),
                ('latest', models.BooleanField(default=False)),
                ('best_seller', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookType')),
                ('suppliers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.SuppliersDetail')),
            ],
        ),
    ]
