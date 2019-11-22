from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from book.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from taggit.models import Tag, TaggedItem


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

# Below code is for Search Ebook which fetch the data using Tags ID
# class Search(APIView):
#     def get_object(self, id):
#         try:
#             return TaggedItem.objects.filter(tag_id=id)
#         except TaggedItem.DoesNotExist:
#             return Response({'Error': 'Given Object Not Available'}, status=404)
#
#     def get(self, request, id=None):
#         instanceobj = self.get_object(id)
#         print(type(instanceobj), instanceobj)
#
#
#         # for i in instanceobj:
#         #     # ebookid = []
#         #     # ebookid.append(i.object_id)
#         #     # print(ebookid)
#         #     ebookid = i.object_id
#         #     ebookobj = EBook.objects.get(id=ebookid)
#         #     data = []
#         #     data.append(i.object_id)
#         #     # print(type(ebookobj), ebookobj)
#         #     print(data)
#
#         return render(request, 'success.html', {'Ebookobj': instanceobj})
#         # return Response(serialized.data)


# Below code is for Search Ebook which fetch the data using Tags NAME
def searchfn(request, name):
    global id
    if request.method == 'GET':
        tagname = Tag.objects.filter(name=name)
        # id = tagname.id
        for i in tagname:
            id = i.id
        print(id)
        taggeditem = TaggedItem.objects.filter(tag_id=id)
        print(taggeditem)
        return render(request, 'success.html')