from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from event.models import Event
from users.models import User
from lamkprs.form import ParticipantTypeForm,CPDForm
from event.models import ParticipantType,CPD
from django.contrib import messages
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
def viewParticipantType(request,pk):
    event = Event.objects.get(id=pk)
    participantType = ParticipantType.objects.filter(event_id=event.id)
    context = {'types':participantType,'event':event}
    return render(request,'adminpanel/participant-type.html',context)

@user_passes_test(is_staff)
def viewCPD(request,pk):
    event = Event.objects.get(id=pk)
    cpd = CPD.objects.filter(event_id=event.id)
    context = {'cpd':cpd,'event':event}
    return render(request,'adminpanel/cpd.html',context)

@user_passes_test(is_staff)
def addCPD(request,pk):
    name = 'Add CPD'
    event =  Event.objects.get(id=pk)
    user = User.objects.get(id=request.user.id)
    form = CPDForm()
    if request.method =="POST":
            form = CPDForm(request.POST)
            if form.is_valid():
                cpd = form.save(commit=False)
                cpd.event = event
                cpd.user = user
                cpd.save()
                return redirect('cpd',event.id)
            else:
                messages.error(request,form.errors)
    context = {'form':form,'name':name}
    return render(request,'form.html',context)

@user_passes_test(is_staff)
def addParticipantType(request,pk):
    name = 'Add Participant Type'
    event =  Event.objects.get(id=pk)
    form = ParticipantTypeForm()
    if request.method =="POST":
            form = ParticipantTypeForm(request.POST)
            if form.is_valid():
                participant_type = form.save(commit=False)
                participant_type.event = event
                participant_type.save()
                return redirect('participant-type',event.id)
            else:
                messages.error(request,form.errors)
    context = {'form':form,'name':name}
    return render(request,'form.html',context)

