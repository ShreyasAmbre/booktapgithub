from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


def homepage(request):
    return render(request, 'index.html')


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


