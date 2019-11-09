from rest_framework import status

from favourite.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from favourite.models import WishList
# Create your views here.
@api_view(['GET'])
def getwishlist(request):
    if request.method == 'GET':
        user_data = WishList.objects.all()
        serializer = WishListSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def postwishlist(request):
    if request.method == 'GET':
        data = {
            'user_id': 80,
            'book_id': 5,
        }
        serializer = WishListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)