from favourite.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from favourite.models import WishList
# Create your views here.
@api_view(['GET'])
def wishlist(request):
    if request.method == 'GET':
        user_data = WishList.objects.all()
        serializer = WishListSerializer(user_data, many=True)
        return Response(serializer.data)