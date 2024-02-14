from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
# Extend user model to hold customer phonenumbers
class Customer(AbstractUser):
    phonenumber = models.CharField(max_length=12, unique=True)
    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

    objects = UserManager()