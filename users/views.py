from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'error in login')
            return redirect('login')
    else:
        return render(request, 'login.html',)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       email = request.POST['email']
       if User.objects.filter(username=username).exists():
        messages.info(request,'error')
        return redirect('signup')
       else:
        user= User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html',)



@login_required
def logoutt(request):
    auth.logout(request)
    return redirect('login')


