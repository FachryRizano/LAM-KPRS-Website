from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from event.models import Event
from users.models import User
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email','no_wa','password1','password2']
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            ) 
        return cleaned_data