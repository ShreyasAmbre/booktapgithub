from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from book.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from taggit.models import Tag

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
        user_data = EBook.objects.all()
        serializer = EBookSerializer(user_data, many=True)
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


@api_view(['GET'])
def novelsebook(request):
    if request.method == 'GET':
        novel_ebooks = EBook.objects.filter(category_id=1)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def adventureebook(request):
    if request.method == 'GET':
        novel_ebooks = EBook.objects.filter(category_id=2)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def autobiographyebook(request):
    if request.method == 'GET':
        novel_ebooks = EBook.objects.filter(category_id=3)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


class EbookView(APIView):
    def get_object(self, id):
        try:
            return EBook.objects.get(id=id)
        except EBook.DoesNotExist:
            return Response({'Error': 'Given Object Not Available'}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serialized = EBookSerializer(instance)
        return Response(serialized.data)

