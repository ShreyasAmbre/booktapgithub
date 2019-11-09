from django.db import models
from django.db import models
from taggit.managers import TaggableManager

from pro.models import Signin
from supplier.models import SuppliersDetail


class BookType(models.Model):
    category_name = models.CharField(max_length=50)


class Book(models.Model):
    suppliers_id = models.ForeignKey(SuppliersDetail, on_delete=models.CASCADE)
    category_id = models.ForeignKey(BookType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ImageField(upload_to='booksimages')
    book = models.FileField(upload_to='book')
    price = models.IntegerField()
    edition = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    publication_name = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)
    features = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)


class EBook(models.Model):
    suppliers_id = models.ForeignKey(SuppliersDetail, on_delete=models.CASCADE)
    category_id = models.ForeignKey(BookType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ImageField(upload_to='booksimages')
    book = models.FileField(upload_to='ebook')
    edition = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    publication_name = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)
    features = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    original_price = models.IntegerField()
    booktap_price = models.IntegerField()
    tags = TaggableManager()
    format = models.CharField(max_length=50)
    file_size = models.FloatField()
    isbn = models.CharField(max_length=50)
    book_rated = models.IntegerField()


class BookReviewRecord(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    ebook_id = models.ForeignKey(EBook, on_delete=models.CASCADE)
    reviews = models.TextField()
    rating = models.IntegerField()