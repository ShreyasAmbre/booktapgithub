from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.models import User, auth

# API Imports
from rest_framework import status

from customer.serializers import CustomerReviewSerializer
from pro.models import Signin
from pro.serializers import SigninSerializer, UserSerializer
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


@api_view(['GET', 'POST'])
def register(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username', "")
    #     firstname = request.POST.get('firstname', False)
    #     lastname = request.POST.get('lastname', False)
    #     email = request.POST.get('email', False)
    #     contact = request.POST.get('email', False)
    #     customer = request.POST.get('customer', False)
    #     supplier = request.POST.get('supplier', False)
    #     password1 = request.POST.get('password1', False)
    #
    #     user = User.objects.create_user(username=username, email=email, password=password1)
    #     user.save()
    #
    #     userid = User.objects.get(username=username)
    #     userprofile = Signin.objects.create(user=userid, first_name=firstname, last_name=lastname, contact=contact,
    #                                         is_customer=customer, is_suppliers=supplier)
    #     userprofile.save()
    #
    #     return render(request, 'profile.html')
    # else:
    #     return render(request, 'register.html')

    if request.method == 'POST':
        # username = request.POST.get('username', "")
        # email = request.POST.get('email', False)
        # password1 = request.POST.get('password1', False)
        #
        # firstname = request.POST.get('firstname', False)
        # lastname = request.POST.get('lastname', False)
        # contact = request.POST.get('email', False)
        # # customer = request.POST.get('customer', False)
        # # supplier = request.POST.get('supplier', False)
        # userdata = {
        #     'username': username,
        #     'email': email,
        #     'is_staff': True,
        #     'is_superuser': True,
        #     'password': make_password(password1),
        # }

        userserializer = UserSerializer(data=request.data)

        if userserializer.is_valid():
            userserializer.save()
            userid = User.objects.get(username=request.data.username)
            print(userid, type(userid))
            if userid:
                # id = userid.id
                # print(id)
                # userprofiledata = {
                #     'user': id,
                #     'first_name': firstname,
                #     'last_name': lastname,
                #     'contact': contact,
                # }
                userprofileserializer = SigninSerializer(data=request.data)
                print(userprofileserializer)
                if userprofileserializer.is_valid():
                    userprofileserializer.save()
                    return Response(userprofileserializer.data, status=status.HTTP_201_CREATED)
                return Response(userprofileserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'register.html')


@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # auth.login(request, user)
            # try:
            #     instance = User.objects.get(username=username)
            # except Signin.DoesNotExist:
            #     return Response({'Errors': 'Object not found'}, status=404)
            #
            # serialized = UserSerializer(instance)
            # return Response(serialized.data)
            # # return render(request, 'profile.html', {'Serialized': serialized})

            userobj = User.objects.get(username=username)
            print(type(userobj), userobj, ':- Printed from Pro views.py')
            return render(request, 'customer.html', {'USER': userobj})
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


