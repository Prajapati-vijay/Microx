from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import User
import requests
import json
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

def jsign(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get('Phone')
        password=request.POST.get('password')
        option=request.POST.get('choice')
        if not name or not username or not password or not option:
            messages.success(request,"Please enter the complete details ")
            return render(request,"signup.html")
        c=User.objects.filter(username=username)
        if c:
            messages.success(request,"Mobile number already exist !")
            return render(request,"signup.html")
        user=User.objects.create_user(username,password)


        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        res= requests.get( "http://ip-api.com/json/42.111.37.31")
        data=res.text
        dic=json.loads(data)
        if dic["status"]=="fail":
            user.lat=float("0.0")
            user.lng=float("0.0")
        else:
            user.lat=float(dic["lat"])
            user.lng=float(dic["lon"])
        print(dic)
        if option=='1':
            user.j_mode="watchman"
            print(option)
        elif option=='2':
            user.j_mode="maid"
            print(option)
        elif option=='3':
            user.j_mode="care"
            print(option)
        user.w_mode="job"
        user.first_name=name
            
        user.save()
        messages.success(request,"Your account has been created successfully ")
        return render(request,"signup.html")
    #if request.method=="POST":
    return render(request,"signup.html") 

def esign(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get('Phone')
        password=request.POST.get('password')
        if not name or not username or not password:
            messages.success(request,"Please enter the complete details ")
            return render(request,"signup.html")
        c=User.objects.filter(username=username)
        if c:
            messages.success(request,"Mobile number already exist !")
            return render(request,"signup.html")
        user=User.objects.create_user(username,password)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        res= requests.get( "http://ip-api.com/json/"+ip)
        data=res.text
        dic=json.loads(data)
        if dic["status"]=="fail":
            user.lat=float("0.0")
            user.lng=float("0.0")
        else:
            user.lat=float(dic["lat"])
            user.lng=float(dic["lon"])
        print(dic)
        user.w_mode="hire"
        user.first_name=name
            
        user.save()
        messages.success(request,"Your account has been created successfully")
        return render(request,"signup.html")
    return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        phone=request.POST.get("Phone")
        password=request.POST.get("password")
        
        user = authenticate(username=phone, password=password)
        if user is not None:
            
            auth.login(request,user)
            if request.user.w_mode=="job":
                return redirect("/map1/") 
            elif request.user.w_mode=="hire":

                return redirect("/map/") 
        else:
            
            return HttpResponse("the password is not right")

    return render(request,"login.html")

def logout(request):
    auth.logout(request) 
    return redirect("/home/")

