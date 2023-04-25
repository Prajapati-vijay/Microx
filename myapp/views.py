from django.shortcuts import render,redirect
from django.http import HttpResponse
import folium
from account.models import User
import haversine as hs
from django.contrib import messages
from .models import jobpost,apply,contactinfo
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

@login_required(login_url="/home/")
def profile(request):
    i=request.user.username
    s=apply.objects.filter(job_seeker_No=i)
    j=jobpost.objects.all()
    return render(request,"profile.html",{"j":j,"s":s})

@login_required(login_url="/home/")
def profilee(request):
    number=request.user.id
    c=request.user.username
    s=apply.objects.filter(Employer_No=c)
    j=jobpost.objects.filter(user_id=number)
    return render(request,"profile_emp.html",{"j":j,"s":s}) 


def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        msg=request.POST.get("msg")
        obj=contactinfo()
        obj.name=name
        obj.phone=phone
        obj.msg=msg
        obj.save()
        messages.success(request,"Your query has been sent successfully ! we will be back to you shortly")
        return redirect("/contact/")
        
    return render(request,"contact.html")

def news(request):
    return render(request,"news.html")

@login_required(login_url="/home/")
def show_map(request):  
    if request.method=="POST":
        choice=request.POST.get("choice")
        if choice=="1":
            s=User.objects.filter(j_mode="maid")
        elif choice=="2":
            s=User.objects.filter(j_mode="watchman")
        elif choice=="3":
            s=User.objects.filter(j_mode="care")
        print(choice)
    #creation of map comes here + business logic
        
        m = folium.Map([28.4744, 77.5040], zoom_start=15)
        for i in s:
           
            
            folium.Marker(
                location=[i.lat,i.lng],
                popup='Mt. Hood Meadows',
                zoom_start=12,
                icon=folium.Icon(icon='cloud')
            ).add_to(m)
        test = folium.Html('<b>Hello world</b>', script=True)
        popup = folium.Popup(test, max_width=2650)
        folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
        m=m._repr_html_() #updated
        context = {'my_map': m}
 
        return render(request, 'interface.html', context)
    #Handeling the get request 
    if request.method=="GET":

         p=User.objects.filter(is_superuser=False)
         m = folium.Map([28.4744, 77.5040], zoom_start=8)
         lat=request.user.lat
         lng=request.user.lng
        
         for i in p:
            if i.lat==request.user.lat and i.lng==request.user.lng:
                folium.Marker(
            location=[i.lat,i.lng],
                popup='Mt. Hood Meadows',
                 icon=folium.Icon(color='red')
            ).add_to(m)

            else:


                folium.Marker(
            location=[i.lat,i.lng],
                popup='Mt. Hood Meadows',
                zoom_start=12,
                icon=folium.Icon(icon='cloud')
                ).add_to(m)
            

         test = folium.Html('<b>Hello world</b>', script=True)
         popup = folium.Popup(test, max_width=2650)
         folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
         m=m._repr_html_() #updated
         context = {'my_map': m}
 
         return render(request, 'interface.html', context)


# Storing the data of job posted by the employer

def job(request):
    if request.method=="POST":
        choice=request.POST.get("choice")
        amt=request.POST.get("amount")
        a=jobpost()
        if choice=="1":
            a.catagory="maid"
        elif choice=="2":
            a.catagory="watchman"
        elif choice=="3":
            a.catagory="care"

        a.amount=amt
        b=request.user.first_name
        p=request.user.username
        a.name=b
        a.user=request.user
        a.phone=p   
        a.save()
        messages.success(request,"You have posted the job successsfully")
        return redirect("/map/")

def map1(request):
    if request.method=="GET":

         p=User.objects.filter(is_superuser=False)
         m = folium.Map([28.4744, 77.5040], zoom_start=8)
         lat=request.user.lat
         lng=request.user.lng
         j=jobpost.objects.all()
         for i in p:
           
            if i.lat==request.user.lat and i.lng==request.user.lng:
                folium.Marker(
            location=[i.lat,i.lng],
                popup='Mt. Hood Meadows',
                 icon=folium.Icon(color='red')
            ).add_to(m)

            else:


                folium.Marker(
            location=[i.lat,i.lng],
                popup='Mt. Hood Meadows',
                zoom_start=12,
                icon=folium.Icon(icon='cloud')
                ).add_to(m)
            

         test = folium.Html('<b>Hello world</b>', script=True)
         popup = folium.Popup(test, max_width=2650)
         folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
         m=m._repr_html_() #updated
         context = {'my_map': m}
 
         return render(request, 'interface1.html', {'my_map': m,"j":j})
    if request.method=="POST":
        a=request.POST.get("choice")
        b=request.POST.get("choice1")
        if a=="1":
            choice="maid"
        if a=="2":
            choice="watchman"
        if a=="3":
            choice="care"
        if b=="1":
            choice1=5
        if b=="2":
            choice1=15
        if b=="3":
            choice1=30
        

        job=jobpost.objects.filter(catagory=choice)
        p=User.objects.filter(w_mode="hire")
        m = folium.Map([28.4744, 77.5040], zoom_start=8)
        lat=request.user.lat
        lng=request.user.lng
     
        for i in p:
            for j in job:
                if i.username==j.phone:
                    loc1=(request.user.lat,request.user.lng)
                    loc2=(i.lat,i.lng)
                    length=hs.haversine(loc1,loc2)
                    if length<=choice1:
           
                        if i.lat==request.user.lat and i.lng==request.user.lng:
                            folium.Marker(
                            location=[i.lat,i.lng],
                            popup='Mt. Hood Meadows',
                            icon=folium.Icon(color='red')
                            ).add_to(m)

                        else:


                            folium.Marker(
                            location=[i.lat,i.lng],
                            popup='Mt. Hood Meadows',
                            zoom_start=12,
                            icon=folium.Icon(icon='cloud')
                            ).add_to(m)
            

        test = folium.Html('<b>Hello world</b>', script=True)
        popup = folium.Popup(test, max_width=2650)
        folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
        m=m._repr_html_() #updated
        context = {'my_map': m}
 
        return render(request, 'interface1.html', {'my_map': m,"j":j})
 
          

    


def applyjob(request,id):

    
    s=apply()
    n=jobpost.objects.get(id=id)
   
    nam=n.name
    s.Employer_Name=nam
    s. Employer_No=n.user
    s.catagory=n.catagory
    s.job_seeker_Name=request.user.first_name
    s.job_seeker_No=request.user
    s.job_id=id
    s.save()
    messages.success(request,"You have successfully Applied for this job ")
    return redirect("/profile/")


def accept(request,id):
    a=apply.objects.get(id=id)

    a.status="Accepted"
    a.save()
    messages.success(request,"You have successfully Accepted the application")
    return redirect("/profilee/")

        
def reject(request,id):
    a=apply.objects.get(id=id)
    a.status="Rejected"
    a.save()  
    messages.info(request,"You have successfully Rejected  the application")  
    return redirect("/profilee/")


def delet(request,id):
    d=jobpost.objects.get(id=id)
    check=apply.objects.filter(job_id=id)
    if check:
        check.delete()
    d.delete()
    messages.success(request,"job deleted successfully ! ")
    return redirect("/profilee/")



        
 