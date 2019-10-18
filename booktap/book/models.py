from django.db import models
from django.db import models
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
    price = models.IntegerField()
    edition = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    publication_name = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)
    features = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)


class BookReviewRecord(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    reviews = models.TextField()