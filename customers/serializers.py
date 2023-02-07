from dataclasses import field
from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from velma_backend.settings import  BASE_DOMAIN


class CompanySerializer(serializers.ModelSerializer):
    extra_kwargs = {
            'id': {'read_only': True}
        }
    class Meta:
        model = Company
        fields ='__all__'

    def create(self, validated_data):
        schema_name = validated_data.get('schema_name')
        name = validated_data.get('name')
        address = validated_data.get('address')
        phone_number = validated_data.get('phone_number')
        email = validated_data.get('email')
        contact_person = validated_data.get('contact_person')
        industry = validated_data.get('industry')
        size = validated_data.get('size')
        status = validated_data.get('status')
        sub_domains = validated_data.get('sub_domains')

        tenant = Company(schema_name=schema_name,name=name,address=address,phone_number=phone_number,email=email,contact_person=contact_person,industry=industry,size=size,status=status,sub_domains=sub_domains)
        tenant.save()
        # sd = sub_domains+BASE_DOMAIN
        domain = Domain()
        domain= Domain.objects.create(domain=sub_domains , tenant=tenant,is_primary=True)
        # domain.domain(sub_domains)
        # domain.tenant = tenant
        # domain.is_primary = True
        # domain.save()

        return tenant