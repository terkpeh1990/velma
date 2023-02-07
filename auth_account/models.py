from django.contrib.auth.models import AbstractUser
from django.db import models
from customers.models import  Company


class User(AbstractUser):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    company_id =models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name