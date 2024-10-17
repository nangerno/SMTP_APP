from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Group
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username=None
    id=models.IntegerField(primary_key=True)
    email= models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects=CustomUserManager()
