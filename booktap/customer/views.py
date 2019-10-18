from django.shortcuts import render
# API Imports
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
def customersearch(request):
    if request.method == 'GET':
        user_data = CustomerSearch.objects.all()
        serializer = CustomerSearchSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def customerreview(request):
    if request.method == 'GET':
        user_data = CustomerReview.objects.all()
        serializer = CustomerReviewSerializer(user_data, many=True)
        return Response(serializer.data)
