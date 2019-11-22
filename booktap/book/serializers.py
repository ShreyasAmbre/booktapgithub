from rest_framework import serializers
from taggit.models import TaggedItem

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


class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'


class TaggedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = '__all__'