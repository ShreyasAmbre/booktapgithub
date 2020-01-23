from rest_framework import serializers
from VideoBook.models import *


class VideoBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBook
        fields = '__all__'


class VideoBookReviewRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBookReviewRecord
        fields = '__all__'


class VideoBookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBookReviewRecord
        fields = '__all__'