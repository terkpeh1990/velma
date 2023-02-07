from dataclasses import field
from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class SuppliersSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            'id': {'read_only': True}
        }
    class Meta:
        model = Suppliers
        fields ='__all__'