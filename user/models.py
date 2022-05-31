from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  age = models.PositiveIntegerField(null=True,blank=True)
  address = models.TextField()


