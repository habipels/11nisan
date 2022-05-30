from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
from .forms import *
def giris(request):
    form = Login_form(request.POST or None)
    content = {"form":form}
    if form.is_valid():
        usernamee = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=usernamee , password =password)
        if user is None :
            return render(request,"user_temp/login.html",content)
        login(request,user)
        return redirect("index")
    return render(request,"user_temp/login.html",content)
def cikis(request):
    logout(request)
    return redirect("index")
def kayit(request):
    form = Register_form(request.POST or None)
    content = {"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        yeni_kullanici = User(username = username,email=email)
        yeni_kullanici.set_password(password)
        yeni_kullanici.save()
        login(request,yeni_kullanici)
        return redirect("index")
    return render(request,"user_temp/register.html",content)
