from django.db import models
# from tenant_users.tenants.models import TenantBase
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.postgres.fields import HStoreField
import uuid


# Create your models here.
class Company(TenantMixin):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250,null=True,blank=True)
    address = HStoreField(null=True, blank=True)
    phone_number = models.CharField(max_length=250,null=True,blank=True)
    email = models.CharField(max_length=250,null=True,blank=True)
    contact_person = HStoreField(null=True, blank=True)
    industry = models.CharField(max_length=250,null=True,blank=True)
    size = models.CharField(max_length=250,null=True,blank=True)
    status = models.CharField(max_length=250,null=True,blank=True)
    sub_domains = models.CharField(max_length=250,null=True,blank=True)
    schema_name = models.CharField(max_length=250,null=True,blank=True)

    # auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass