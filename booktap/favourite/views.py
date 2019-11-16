from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from favourite.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from favourite.models import WishList
# GET all WISHLIST's of ALL USERS
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


# Get The WishList of particular USER only which will require User Id and that User having partular WishList
class SingleUserFavoriteListView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'Error': 'Given Object Not Available'}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        id = instance.id
        print(id)
        user_data = WishList.objects.filter(user_id=id)
        print(user_data)
        serializer = WishListSerializer(user_data, many=True)
        return Response(serializer.data)
        # return render(request, 'success.html')