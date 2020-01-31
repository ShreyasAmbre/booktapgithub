from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=20)
    cutomer = models.BooleanField()
    supplier = models.BooleanField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    designation = models.CharField(max_length=50)
