from django.urls import path,include
from django.shortcuts import render
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
]
