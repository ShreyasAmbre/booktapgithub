from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

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
def getbookreviewrecords(request):
    if request.method == 'GET':
        user_data = BookReviewRecord.objects.all()
        serializer = BookReviewRecordSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def postbookreviewrecords(request):
    if request.method == 'GET':
        data = {
            'user_id': 80,
            'ebook_id': 2,
            'reviews': "Very Bad",
            'rating': 4,
        }
        serializer = BookReviewRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class bookreviewrecords(APIView):
#
#     def get(self, request, format=None):
#         snippets = BookReviewRecord.objects.all()
#         serializer = BookReviewRecordSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#
#         # userobj = User.objects.get(id=id)
#         # ebookobj = Ebook.objects.get(id=id)
#         data = {
#             'user_id_id': 1,
#             'ebook_id_id': 2,
#             'reviews': "Done",
#             'rating': 4,
#         }
#         serializer = BookReviewRecordSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
