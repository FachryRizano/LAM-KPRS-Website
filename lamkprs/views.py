from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,'home.html')

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =="POST":
        username = request.POST.get('username').lower()
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
        

    context = {'page':page}
    return render(request,'login_register.html',context)

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('home')



def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error has been occured')
    context = {'form':form}
    return render(request,'login_register.html',context)
