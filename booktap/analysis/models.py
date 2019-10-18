from django.db import models


class Count(models.Model):
    book_count = models.IntegerField()
    customer_count = models.IntegerField()
    supplier_count = models.IntegerField()
    order_success_count = models.IntegerField()