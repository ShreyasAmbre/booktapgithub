from django.db import models
from ElectronicBook.models import Book


class Discount(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    percentage = models.FloatField()