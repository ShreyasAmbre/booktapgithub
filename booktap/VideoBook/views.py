from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import CustomerReview
from VideoBook.models import VideoBook, VideoBookReviewRecord
from VideoBook.serializers import VideoBookSerializer, VideoBookReviewRecordSerializer


# Create your views here.
def videobooks(request):
    return render(request, 'success.html')


# GET ALL Videos Books DETAILS
@api_view(['GET'])
def getvideobooks(request):
    if request.method == 'GET':
        user_data = VideoBook.objects.all()
        serializer = VideoBookSerializer(user_data, many=True)
        return Response(serializer.data)


# GET API Gives only Signle Video Book Record which is requested
class VideoBookView(APIView):
    def get_object(self, id):
        try:
            return VideoBook.objects.get(id=id)
        except VideoBook.DoesNotExist:
            return Response({'Error': 'Given Object Not Available'}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serialized = VideoBookSerializer(instance)
        return Response(serialized.data)


# POST API for  CUstomer Review
@api_view(['GET'])
def postbookreviewrecords(request):
    if request.method == 'GET':
        # data = {
        #     'user_id': 80,
        #     'ebook_id': 2,
        #     'reviews': "Very Bad",
        #     'rating': 4,
        # }
        serializer = VideoBookReviewRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET API of All Reviews of all Video Boooks
@api_view(['GET'])
def getvideobookreviewrecords(request):
    if request.method == 'GET':
        user_data = VideoBookReviewRecord.objects.all()
        serializer = VideoBookReviewRecordSerializer(user_data, many=True)
        return Response(serializer.data)


# 5 Star Rating Code is here Individual Book Rating is updated
def ratedfn(request, id):
    global rating, res, value
    customerratings = CustomerReview.objects.filter(videobook_id=id)
    print(customerratings)
    arr = []
    for i in customerratings:
        rating = i.rating
        arr.append(rating)
        sumdata = sum(arr)
        customercount = len(arr)
        totalratings = customercount * 5
        value = sumdata / totalratings
        res = value * 5
        # print(result)

    print("Result", res)
    videobookobj = VideoBook.objects.get(id=id)
    ebookratingcolumvalue = videobookobj.book_rated
    print("Before Value", ebookratingcolumvalue)
    videobookobj.book_rated = res
    print(videobookobj.book_rated)
    videobookobj.save()
    updatedvideobookobj = VideoBook.objects.get(id=id)
    updatedrattingvalue = updatedvideobookobj.book_rated
    print("Updated Value", updatedrattingvalue)
    return render(request, 'success.html')


@api_view(['GET'])
def search(request, name):
    print(name)
    value = VideoBook.objects.annotate(search=SearchVector('name', 'discription'),).filter(search=name)
    print(value)
    return render(request, "success.html", {'Value': value})


class SearchList(generics.ListAPIView):
    serializer_class = VideoBookSerializer

    # def get_queryset(self):
    #     queryset = VideoBook.objects.all()
    #     name = self.request.query_params.get('name', None)
    #     print(name)
    #     if name is not None:
    #         queryset = queryset.filter(name=name)
    #         print("*****************************")
    #     return queryset

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        name = self.kwargs['name']
        queryset = VideoBook.objects.annotate(search=SearchVector('name', 'discription'),).filter(search=name)
        return queryset