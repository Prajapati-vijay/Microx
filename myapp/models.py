from django.db import models
from account.models import User

class jobpost(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=False,blank=False ,default=None)    
    catagory=models.CharField(max_length=10,unique=False)
    amount=models.IntegerField(unique=False)
    phone=models.CharField(max_length=10)

# Create your models here. 

class apply(models.Model):
    Employer_Name=models.CharField(max_length=50,blank=False ,default=None)
    job_seeker_Name=models.CharField(max_length=50,blank=False ,default=None)
    Employer_No=models.CharField(max_length=50,blank=False ,default=None)
    job_seeker_No=models.CharField(max_length=50,blank=False ,default=None)
    catagory=models.CharField(max_length=15,blank=False ,default=None)
    job_id=models.CharField( max_length=10)
    status=models.CharField(max_length=15,blank=True ,null=True,default=None)



class contactinfo(models.Model):
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    msg=models.TextField(max_length=100)   
