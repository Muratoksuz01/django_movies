from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    filimler=Movie.objects.all()
    return render(request,'pages/index.html', {"movies":filimler})
def about(request,pk):
    movie=Movie.objects.get(id=pk)
    return render(request,'pages/about.html', {"movie":movie})





def rlogin(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(username=username,password=password)

    if user is not None:
        login(user)
    filimler=Movie.objects.all()
    return render(request,'pages/index.html', {"movies":filimler})
def register(request):
    username=request.POST["username"]
    email=request.POST["email"]
    password=request.POST["password"]
    repassword=request.POST["repassword"]
    gender=request.POST["gender"]
    profil=request.POST["profil"]
    print(profil)
    print(gender)
    print(request.POST)

    if repassword==password:
        user=User.objects.create_user(username=username,email=email,password=password,gender=gender,profil=profil)
        user.save()


    filimler=Movie.objects.all()
    return render(request,'pages/index.html', {"movies":filimler})