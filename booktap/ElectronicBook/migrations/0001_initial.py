# Generated by Django 2.2.5 on 2019-12-04 06:44

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('pro', '0022_auto_20191203_0717'),
        ('supplier', '0002_suppliersrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='booksimages')),
                ('book', models.FileField(upload_to='ebook')),
                ('edition', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('publication_name', models.CharField(max_length=50)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('features', models.BooleanField(default=False)),
                ('latest', models.BooleanField(default=False)),
                ('best_seller', models.BooleanField(default=False)),
                ('original_price', models.IntegerField()),
                ('booktap_price', models.IntegerField()),
                ('format', models.CharField(max_length=50)),
                ('file_size', models.FloatField()),
                ('isbn', models.CharField(max_length=50)),
                ('book_rated', models.FloatField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElectronicBook.BookType')),
                ('suppliers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.SuppliersDetail')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='BookReviewRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('rating', models.IntegerField()),
                ('ebook_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElectronicBook.ElectronicBook')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Signin')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
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
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ElectronicBook.BookType')),
                ('suppliers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.SuppliersDetail')),
            ],
        ),
    ]