from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import auth
# API Imports
from rest_framework.parsers import JSONParser

from pro.models import Signin
from pro.serializers import SigninSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# API:- We get Data of All User only through API no need of login
@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        user_data = Signin.objects.all()
        serializer = SigninSerializer(user_data, many=True)
        return Response(serializer.data)


# API:- We get Data of All User only through API only after Login
@api_view(['GET', 'POST'])
def userlist(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            user_data = Signin.objects.all()
            serializer = SigninSerializer(user_data, many=True)
            return Response(serializer.data)

            # return redirect('/')
            # return render(request, 'profile.html', {'Username': user})

    else:
        # return render(request, 'error.html', {'error': 'Login Failed'})
        return render(request, 'login.html')
    return render(request, 'profile.html')


# API:- We get Data of Current User only through API only after Login
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            try:
                instance = Signin.objects.get(username=username)
            except Signin.DoesNotExist:
                return Response({'Errors': 'Object not found'}, status=404)
            # user_data = Signin.objects.all()
            # serializer = SigninSerializer(user_data, many=True)
            # return Response(serializer.data)

            serialized = SigninSerializer(instance)
            return Response(serialized.data)

            # return redirect('/')
            # return render(request, 'profile.html', {'Username': user})
    else:
        # return render(request, 'error.html', {'error': 'Login Failed'})
        return render(request, 'login.html')
    return render(request, 'profile.html')


def register(request):
    # username = request.POST['username']
    # email = request.POST['email']
    # contact = request.POST['contact']
    # password1 = request.POST['password1']
    # password2 = request.POST['password2']

    if request.method == 'POST':
        username = request.POST.get('username', "")
        email = request.POST.get('email', False)
        contact = request.POST.get('contact', False)
        customer = request.POST.get('customer', False)
        supplier = request.POST.get('supplier', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)

        user = Signin.objects.create(username=username, email=email, contact=contact, password1=password1,
                                     password2=password2, is_customer=customer, is_suppliers=supplier)
        user.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')



