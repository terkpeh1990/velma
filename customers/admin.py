from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from customers.models import Company

@admin.register(Company)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('id', 'name','phone_number','email','industry','size','status')
