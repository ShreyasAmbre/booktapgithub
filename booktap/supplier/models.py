from django.db import models
from pro.models import Signin
# from book.models import Book


class SuppliersDetail(models.Model):
    user_id = models.ForeignKey(Signin, on_delete=models.CASCADE)
    address = models.TextField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    company_name = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    upi_id = models.CharField(max_length=50)


class SuppliersRecord(models.Model):

    supplier_id = models.ForeignKey(SuppliersDetail, on_delete=models.CASCADE)
    # book_id = models.ForeignKey(Book, on_delete=models.CASCADE)