from django.db import models
from book.models import Book
from pro.models import Signin


class WishList(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)