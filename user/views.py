from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user.models import User
from .register import UserForm

# Create your views here.
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'user/register.html',context)

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(name=username)
        except:
            messages.error(request,"User doesn't exist")

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password doesn't exist")
        user = authenticate(request,username=username,password=password)


    context = {}
    return render(request,'user/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def updateProfile(request):
    return render(request,'user/edit-profile.hmtl')