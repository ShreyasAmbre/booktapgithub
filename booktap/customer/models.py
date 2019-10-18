from django.db import models
from book.models import Book
from pro.models import Signin
from supplier.models import SuppliersDetail


class CustomerOrders(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(SuppliersDetail, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    commission = models.IntegerField()
    remaining = models.IntegerField()


class CustomerSearch(models.Model):
    customer_search = models.TextField()


class CustomerReview(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviews = models.TextField()
