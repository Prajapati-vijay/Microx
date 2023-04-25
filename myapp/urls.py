"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('signup/',views.signup),
    path('map/',views.show_map),
    path('about/',views.about),
    path('service/',views.service), 
    path('news/',views.news),
    path('contact/',views.contact),
    path('job/',views.job),
    path('map1/',views.map1),
    path('apply/<int:id>',views.applyjob),
    path('profile/',views.profile),
    path('profilee/',views.profilee),
    path('status/<int:id>',views.accept),
    path('status1/<int:id>',views.reject),
    path('delete/<int:id>',views.delet),
    
    
]
