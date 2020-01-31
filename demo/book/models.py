from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    book = models.FileField(upload_to='book')


class EBook(models.Model):
    name = models.CharField(max_length=50)
    book = models.FileField(upload_to='ebook')
