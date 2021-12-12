from django.urls import include,path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('create/',views.createEvent,name='create-event'),
    path('',views.viewAllEvent,name='eventlist'),
    path('<str:pk>/',views.viewEvent)
]