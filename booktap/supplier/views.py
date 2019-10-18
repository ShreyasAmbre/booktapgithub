from supplier.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def suppliersdetails(request):
    if request.method == 'GET':
        user_data = SuppliersDetail.objects.all()
        serializer = SuppliersDetailSerializer(user_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def suppliersrecords(request):
    if request.method == 'GET':
        user_data = SuppliersRecord.objects.all()
        serializer = SuppliersRecordSerializer(user_data, many=True)
        return Response(serializer.data)
