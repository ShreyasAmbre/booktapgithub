from rest_framework import serializers
from supplier.models import *


class SuppliersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersDetail
        fields = '__all__'


class SuppliersRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuppliersRecord
        fields = '__all__'