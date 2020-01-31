from django.db import models


class BookVideo(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='bookvideos')