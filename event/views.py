from django.shortcuts import render,redirect
from .models import Event,Topic
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    events = Event.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()
    context = {'events':events,'topics':topics}
    return render(request,'event/eventlist.html',context)

def updateEvent(request,pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    context = {'form':form}
    return render(request,'event/create-event.html',context)

def deleteEvent(request,pk):
    event = Event.objects.get(id=pk)
    if request.method =='POST':
        event.delete()
        return redirect('eventlist')
    return render(request,'event/delete.html',{'obj':event})