from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='dashboard'),
    path('event/',views.allEvent,name='event'),
    path('member/',views.home,name='member'),
    path('user/',views.home,name='users-account'),
    path('group/',views.home,name='users-group'),
    path('add-participant-type/<str:pk>/',views.addParticipantType,name='add-participant-type'),
]
