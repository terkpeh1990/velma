from django.db import models

# Create your models here.
from django.db import models
# from tenant_users.tenants.models import TenantBase
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.postgres.fields import HStoreField
import uuid


# Create your models here.
class Suppliers(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250,null=True,blank=True)
    address = HStoreField(null=True, blank=True)
    phone_number = models.CharField(max_length=250,null=True,blank=True)


    def __str__(self):
        return self.name