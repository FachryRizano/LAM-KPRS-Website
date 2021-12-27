from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    no_wa = PhoneNumberField(null=False,blank=False,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
