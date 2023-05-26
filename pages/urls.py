from django.contrib import admin
from django.urls import path

from .views import index,about,rlogin,register
urlpatterns = [
   path('',index , name='index'),
   path('about/<int:pk>',about, name='about'),
   path('login',rlogin, name='login'),
   path('register',register, name='register'),

   

] 