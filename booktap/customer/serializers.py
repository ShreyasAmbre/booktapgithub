from rest_framework import serializers
from customer.models import *


class CustomerOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrders
        fields = '__all__'


class CustomerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSearch
        fields = '__all__'


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = '__all__'
