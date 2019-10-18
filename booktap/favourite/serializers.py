from rest_framework import serializers
from favourite.models import *


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'