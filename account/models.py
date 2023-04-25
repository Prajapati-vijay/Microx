from email.policy import default
from enum import unique
from .manager import Usermanager
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username =models.CharField(max_length=10,unique=True,blank=False,default=True)
    
    w_mode=models.CharField(max_length=100,default=False)
    lat=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    j_mode=models.CharField(max_length=100,default=False,blank=False,null=False)
    USERNAME_FIELD='username'
    city=models.CharField(max_length=50,default=None , blank=True,null=True)
    
    
    objects=Usermanager()
    REQUIRED_FIELDS=[]  