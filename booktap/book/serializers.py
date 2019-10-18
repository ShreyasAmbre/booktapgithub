from rest_framework import serializers
from book.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class EBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBook
        fields = '__all__'


class BookReviewRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReviewRecord
        fields = '__all__'
