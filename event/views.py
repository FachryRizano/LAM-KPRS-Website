from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import Event,Topic, Message
from django.db.models import Q
from .event_form import EventForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    if request.method =="POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    context = {'form':form}
    return render(request,'event/create-event.html',context)

@login_required(login_url='login')
def viewEvent(request,pk):
    event = Event.objects.get(id=pk)
    room_messages = event.message_set.all().order_by('-created')
    participants = event.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            event = event,
            body = request.POST.get('body')
        )
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
        
    context = {'event':event,'room_messages':room_messages,'participants':participants}
    return render(request,'event/event.html',context)

@login_required(login_url='login')
def viewAllEvent(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    events = Event.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q)|Q(hosted_by__username__icontains=q))
    topics = Topic.objects.all()
    context = {'events':events,'topics':topics}
    return render(request,'event/eventlist.html',context)

@login_required(login_url='login')
def updateEvent(request,pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.user != event.hosted_by:
        return HttpResponse("You aren't allowed here!")

    if request.method == 'POST':
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventlist')
    context = {'form':form}
    return render(request,'event/create-event.html',context)

@login_required(login_url='login')
def deleteEvent(request,pk):
    event = Event.objects.get(id=pk)
    if request.user != event.hosted_by:
        return HttpResponse("You aren't allowed here!")

    if request.method =='POST':
        event.delete()
        return redirect('eventlist')
    return render(request,'event/delete.html',{'obj':event})

@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("You aren't allowed here!")

    if request.method =='POST':
        message.delete()
        return redirect('event',pk = message.event.id)
    return render(request,'event/delete.html',{'obj':message})
