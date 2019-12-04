from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import User
from django.shortcuts import render
# API Imports
from rest_framework import status
from rest_framework.views import APIView

from ElectronicBook.models import ElectronicBook
from ElectronicBook.serializers import BookReviewRecordSerializer
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


@api_view(['GET', 'POST'])
def postcustomersearch(request):
    if request.method == 'POST':
        # data = {
        #     'customer_search': "Jhone Coner Search",
        # }
        serializer = CustomerSearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET All PAST Review of All EBOOKS
@api_view(['GET'])
def getcustomerreview(request):
    if request.method == 'GET':
        tnow = timezone.now()

        print(tnow)
        user_data = CustomerReview.objects.all().filter(date__lt=tnow).order_by('-date')
        serializer = CustomerReviewSerializer(user_data, many=True)
        return Response(serializer.data)


# POST Review
@api_view(['GET', 'POST'])
def postcustomerreview(request):
    if request.method == 'POST':
        # user = request.POST.get('userobj', "")
        # review = request.POST.get('review', "")
        # ratingint = request.POST.get('rating', "")
        # rating = int(ratingint)
        # # print(type(rating), rating)
        #
        # ebookobj = EBook.objects.get(name="Attitude")
        # ebookid = ebookobj.id
        # # name = user.username
        # # print(type(user), name)
        #
        # data = {
        #     'user_id': user,
        #     'reviews': review,
        #     'book_id': ebookid,
        #     'rating': rating,
        # }
        serializer = CustomerReviewSerializer(data=request.data)

        # bookserializer = BookReviewRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'customer.html')


# GET all REVIEWS of Particular EBOOK Only
class SingleEBookCustomerReviewView(APIView):
    def get_object(self, id):
        try:
            return ElectronicBook.objects.get(id=id)
        except ElectronicBook.DoesNotExist:
            return Response({'Error': 'Given Object Not Available'}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        id = instance.id
        print(id)
        tnow = timezone.now()
        user_data = CustomerReview.objects.filter(Q(book_id=id) & Q(date__lte=tnow))
        print(user_data)
        serializer = CustomerReviewSerializer(user_data, many=True)
        return Response(serializer.data)
        # return render(request, 'success.html')
