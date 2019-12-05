from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from ElectronicBook.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from taggit.models import Tag, TaggedItem
# Create your views here.
from customer.models import CustomerReview


@api_view(['GET'])
def book(request):
    if request.method == 'GET':
        user_data = Book.objects.all()
        serializer = BookSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ebook(request):
    if request.method == 'GET':
        user_data = ElectronicBook.objects.all()
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
        novel_ebooks = ElectronicBook.objects.filter(category_id=1)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def adventureebook(request):
    if request.method == 'GET':
        novel_ebooks = ElectronicBook.objects.filter(category_id=2)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def autobiographyebook(request):
    if request.method == 'GET':
        novel_ebooks = ElectronicBook.objects.filter(category_id=3)
        serializer = EBookSerializer(novel_ebooks, many=True)
        return Response(serializer.data)


class EbookView(APIView):
    def get_object(self, id):
        try:
            return ElectronicBook.objects.get(id=id)
        except ElectronicBook.DoesNotExist:
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


@api_view(['GET'])
def searchfn(request, name):
    global id, EbookData
    if request.method == 'GET':
        tagname = Tag.objects.filter(name=name)
        # id = tagname.id
        for i in tagname:
            id = i.id
        print(id)
        taggeditem = TaggedItem.objects.filter(tag_id=id)
        print(taggeditem)

        arr = []
        objarr = []
        for i in taggeditem:
            data = i.object_id
            # print(data)
            arr.append(data)
            # print(arr)
            for j in arr:
                val = j
                EbookData = ElectronicBook.objects.filter(id=val)
                # print(EbookData)
                # objarr.append(EbookData)
                # print(objarr)
                # for k in EbookData:
                #     author = k.author
                #     print("Author Name is ", author)

        serializer = EBookSerializer(EbookData, many=True)
        # return render(request, 'success.html')
        return Response(serializer.data)


def ratedfn(request, id):
    global rating, res, value
    customerratings = CustomerReview.objects.filter(book_id=id)
    # print(customerratings)
    arr = []
    for i in customerratings:
        rating = i.rating
        arr.append(rating)
        sumdata = sum(arr)
        customercount = len(arr)
        totalratings = customercount * 5
        value = sumdata / totalratings
        res = value * 5
    print("Result", res)
    ebookobj = ElectronicBook.objects.get(id=id)
    ebookratingcolumvalue = ebookobj.book_rated
    print("Before Value", ebookratingcolumvalue)
    ebookobj.book_rated = res
    print(ebookobj.book_rated)
    ebookobj.save()
    updatedebookobj = ElectronicBook.objects.get(id=id)
    updatedrattingvalue = updatedebookobj.book_rated
    print("Updated Value", updatedrattingvalue)
    return render(request, 'success.html')
