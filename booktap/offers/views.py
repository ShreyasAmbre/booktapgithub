from offers.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from offers.models import Discount
from offers.serializers import DiscountSerializer

# Create your views here.
@api_view(['GET'])
def discount(request):
    if request.method == 'GET':
        user_data = Discount.objects.all()
        serializer = DiscountSerializer(user_data, many=True)
        return Response(serializer.data)