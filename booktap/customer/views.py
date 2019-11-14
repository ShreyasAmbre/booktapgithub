from django.contrib.auth.models import User
from django.shortcuts import render
# API Imports
from rest_framework import status

from book.models import EBook
from book.serializers import BookReviewRecordSerializer
from pro.models import Signin
from customer.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Orders
@api_view(['GET'])
def customerorders(request):
    if request.method == 'GET':
        user_data = CustomerOrders.objects.all()
        serializer = CustomerOrdersSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getcustomersearch(request):
    if request.method == 'GET':
        user_data = CustomerSearch.objects.all()
        serializer = CustomerSearchSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def postcustomersearch(request):
    if request.method == 'GET':
        data = {
            'customer_search': "Jhone Coner Search",
        }
        serializer = CustomerSearchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET Revieww
@api_view(['GET'])
def getcustomerreview(request):
    if request.method == 'GET':
        user_data = CustomerReview.objects.all()
        serializer = CustomerReviewSerializer(user_data, many=True)
        return Response(serializer.data)


# POST Review
@api_view(['GET', 'POST'])
def postcustomerreview(request):
    if request.method == 'POST':
        user = request.POST.get('userobj', "")
        review = request.POST.get('review', "")
        ratingint = request.POST.get('rating', "")
        rating = int(ratingint)
        print(type(rating), rating)

        ebookobj = EBook.objects.get(name="Attitude")
        ebookid = ebookobj.id

        data = {
            'user_id': user,
            'reviews': review,
            'book_id': ebookid,
            'rating': rating,
        }
        serializer = CustomerReviewSerializer(data=data)
        # bookserializer = BookReviewRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'customer.html')
