from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import User
from lamkprs.form import UserForm
from django.contrib.auth import authenticate, login, logout
from event.models import Event

def home(request):
    return render(request,'home.html')

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request,email=email,password=password)
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

@login_required(login_url='/login')
def orderEvent(request):
    user = User.objects.get(id=request.user.id)
    order = Event.objects.filter(participants=user)
    context = {'order':order}
    return render(request,'order-list.html',context)




def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,form.errors)
    context = {'form':form}
    return render(request,'login_register.html',context)
