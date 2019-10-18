from rest_framework import serializers
from rest_framework import exceptions
from pro.models import Signin
from django.contrib.auth import authenticate


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = '__all__'


# Below serializer does not have any model it is used for only validation purpose When The Class will called
# class LoginViewSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         username = data.get('username', '')
#         password = data.get('password', '')
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     data['data'] = user
#                 else:
#                     msg = "User is Disabled"
#                     raise exceptions.ValidationError(msg)
#             else:
#                 msg = "Unable to login with given credentails."
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = "Must provide Username and Password"
#             raise exceptions.ValidationError(msg)
#         return data