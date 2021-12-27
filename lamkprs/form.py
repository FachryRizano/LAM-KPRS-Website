from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from event.models import Event
from users.models import User
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['price','participants']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','no_wa','password1','password2']
    