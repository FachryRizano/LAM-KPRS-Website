from django.shortcuts import render,redirect
from .models import Event
from .event_form import EventForm

# Create your views here.
def createEvent(request):
    form = EventForm()
    if request.method =="POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    context = {'form':form}
    return render(request,'event/create-event.html',context)

def viewEvent(request,pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request,'event/event.html',context)

def viewAllEvent(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'event/eventlist.html',context)

# def updateEvent(request,pk):
#     return render(request,)