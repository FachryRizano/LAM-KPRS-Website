from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from event.models import Event
from lamkprs.form import ParticipantTypeForm
# Create your views here.

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def home(request):
    return render(request,'adminpanel/dashboard.html')
    
@user_passes_test(is_staff)
def allEvent(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'adminpanel/event.html',context)

@user_passes_test(is_staff)
def addParticipantType(request):
    form = ParticipantTypeForm()
    context = {'form':form}
    return render(request,'form.html',context)
