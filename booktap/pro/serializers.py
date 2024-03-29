from rest_framework import serializers
from rest_framework import exceptions
from pro.models import Signin, User
from django.contrib.auth import authenticate


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


