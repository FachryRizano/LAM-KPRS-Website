from django.db import models
from user.models import User

class Topic(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

# Create your models here.
class Event(models.Model):
    nama = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    # tanggal = models.DateTimeField()
    # tempat = models.CharField(max_length=100)
    hosted_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # organized_by = models.CharField(max_length=100)
    # event_website = models.CharField(max_length=200) 
    # flyer = models.CharField(max_length=200)
    # peserta= 
    harga = models.IntegerField()
    # deskripsi = models.TextField()
    # counter =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)