from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .decoraters import *
from django.contrib.auth.models import User

@login_required(login_url='/')
def snakeform(request):
    if request.method == "POST":
        return render(request,'accounts/main.html')
    return render(request,'accounts/snakeform.html')

@unauthenticated
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is invalid')
    context={}
    return render(request,'accounts/login.html',context)

@unauthenticated
def register_page(request):
    form=createuserform()
    if request.method=='POST':
        form=createuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created successfully')
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/signup.html',context)

@login_required(login_url='/')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def home_page(request):
    return render(request,'accounts/home.html')

@login_required(login_url='/')
def word_page(request):
    return render(request,'accounts/word.html')

@login_required(login_url='/')
def card_page(request):
    return render(request,'accounts/card.html')

def dashboard_page(request):
    user=User.objects.all()
    count=user.count()
    context={'user':user,'count':count}
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def delete_order(request,pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        user.delete()
        return redirect('dashboard')
    context={'item':user}
    return render(request,'accounts/delete_user.html',context)