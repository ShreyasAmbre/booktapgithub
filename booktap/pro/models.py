from django.contrib.auth.models import User
from django.db import models


class Signin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    contact = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_end_user = models.BooleanField(default=False)
    agree = models.BooleanField(default=False)
    is_customer = models.BooleanField()
    is_suppliers = models.BooleanField()

