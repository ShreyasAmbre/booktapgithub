from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Permission
from passlib.hash import pbkdf2_sha256

# API Imports
from pro.models import Signin
from pro.serializers import SigninSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


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


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        firstname = request.POST.get('firstname', False)
        lastname = request.POST.get('lastname', False)
        email = request.POST.get('email', False)
        contact = request.POST.get('email', False)
        customer = request.POST.get('customer', False)
        supplier = request.POST.get('supplier', False)
        password1 = request.POST.get('password1', False)

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        userid = User.objects.get(username=username)
        userprofile = Signin.objects.create(user=userid, first_name=firstname, last_name=lastname, contact=contact,
                                            is_customer=customer, is_suppliers=supplier)
        userprofile.save()

        return render(request, 'profile.html')
    else:
        return render(request, 'register.html')


@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                instance = User.objects.get(username=username)
            except Signin.DoesNotExist:
                return Response({'Errors': 'Object not found'}, status=404)

            serialized = UserSerializer(instance)
            return Response(serialized.data)
            # return render(request, 'profile.html', {'Serialized': serialized})
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


# API:- Login User Djnago Table API
@api_view(['GET'])
def loginapi(request):
    if request.method == 'GET':
        user_data = User.objects.all()
        serializer = UserSerializer(user_data, many=True)
        return Response(serializer.data)


