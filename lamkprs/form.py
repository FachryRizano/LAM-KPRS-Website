from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from event.models import Event,Participant,ParticipantType
from users.models import User
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['price','participants','status','free_event']
        widgets = {
            'start': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }),
            'end': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }),
        }

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        exclude = ['user','event','code_registration','paid','bill','']

class ParticipantTypeForm(ModelForm):
    class Meta:
        model = ParticipantType
        fields = ['category_name']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','no_wa','password1','password2']
     