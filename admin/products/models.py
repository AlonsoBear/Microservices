from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    
class User(models.Model):
    pass