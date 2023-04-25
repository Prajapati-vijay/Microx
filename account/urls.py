from django.urls import path
from . import views

urlpatterns = [
    path('jsign/',views.jsign),
    path('esign/',views.esign),
    path('login/',views.login),
    path('logout/',views.logout)
    
]