from django.urls import include,path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('create/',views.createEvent,name='create-event'),
    path('',views.viewAllEvent,name='eventlist'),
    path('<str:pk>/',views.viewEvent,name='event'),
    path('update-event/<str:pk>/',views.updateEvent,name='update-event'),
    path('delete-event/<str:pk>/',views.deleteEvent,name='delete-event'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('profile-page/<str:pk>/',views.viewProfile,name='profile-page'),
    path('register/<str:pk>/',views.participantRecapitulation,name='participant-recapitulation')
]