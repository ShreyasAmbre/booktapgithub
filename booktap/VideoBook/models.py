from django.contrib.auth.models import User
from django.db import models
# from supplier.models import SuppliersDetail


# Create your models here.
class VideoBookType(models.Model):
    category = models.CharField(max_length=50)


class VideoBook(models.Model):
    category_id = models.ForeignKey(VideoBookType, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    discription = models.TextField()
    videofile = models.FileField(upload_to='videobooks')
    coverimages = models.FileField(upload_to='coverimages')
    published_date = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50)
    booktap_price = models.IntegerField()
    book_rated = models.FloatField()


class VideoBookReviewRecord(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook_id = models.ForeignKey(VideoBook, on_delete=models.CASCADE)
    reviews = models.TextField()
    rating = models.IntegerField()