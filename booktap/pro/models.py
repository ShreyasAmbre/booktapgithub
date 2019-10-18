from django.db import models


# Create your models here.
class Signin(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contact = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_end_user = models.BooleanField(default=False)
    agree = models.BooleanField(default=False)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    is_customer = models.BooleanField()
    is_suppliers = models.BooleanField()