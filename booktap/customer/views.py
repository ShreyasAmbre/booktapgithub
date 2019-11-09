from django.contrib.auth.models import User
from django.shortcuts import render
# API Imports
from rest_framework import status

from pro.models import Signin
from customer.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
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


@api_view(['GET'])
def getcustomerreview(request):
    if request.method == 'GET':
        user_data = CustomerReview.objects.all()
        serializer = CustomerReviewSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def postcustomerreview(request):
    if request.method == 'POST':
        user = request.POST.get('userobj', "")
        # userobj = User.objects.get(username=user)
        # print(userobj)
        # print(type(userobj))
        # name = request.POST.get('name', "")
        review = request.POST.get('review', "")

        data = {
            'user_id': user,
            'reviews': review,
            'book_id': 5,
            'rating': 1,
        }
        serializer = CustomerReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'customer.html')