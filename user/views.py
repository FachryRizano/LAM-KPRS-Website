from django.shortcuts import render, redirect

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

def login(request):
    return render(request,'user/login.html')

def updateProfile(request):
    return render(request,'user/edit-profile.hmtl')