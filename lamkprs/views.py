from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request,'home.html')

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                raise()
        except:
            messages.error(request,"User doesn't exist")
        

    context = {}
    return render(request,'login.html',context)

@login_required(login_required='/login')
def logoutUser(request):
    logout(request)
    return redirect('home')



def register(request):
    return render(request,'register.html')
