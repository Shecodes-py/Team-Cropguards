from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    state = models.CharField(max_length=30)
    farm_size = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateTimeField(auto_now_add=True)