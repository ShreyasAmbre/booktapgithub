from django.shortcuts import render

from book.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def book(request):
    if request.method == 'GET':
        user_data = Book.objects.all()
        serializer = BookSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ebook(request):
    if request.method == 'GET':
        user_data = Book.objects.all()
        serializer = BookSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def bookreviewrecords(request):
    if request.method == 'GET':
        user_data = BookReviewRecord.objects.all()
        serializer = BookReviewRecordSerializer(user_data, many=True)
        return Response(serializer.data)
