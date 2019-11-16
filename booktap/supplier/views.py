from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView

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


class Profile(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'Error': 'Given Object Not Available'}, status=404)

    def get(self, request, username=None):
        instance = self.get_object(username)
        print(instance)
        return render(request, 'supplierprofile.html')