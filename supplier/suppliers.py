from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from velma_backend.paginator import CustomPagination



class SuppliersViewSet(viewsets.ModelViewSet):
   
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields =['^id','^name']
    ordering_fields = ['id','name']
    ordering = ['-id']