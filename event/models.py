from django.db import models
from users.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(null=True,max_length=100)
    code = models.CharField(max_length=100,default='')
    event_website = models.CharField(max_length=200,null=True,blank=True) 
    no_rek = models.IntegerField(default=0,null=True,blank=True)
    organized_by = models.CharField(max_length=100)
    hosted_by = models.CharField(max_length=100)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    tempat = models.CharField(max_length=100)
    event_pict= models.ImageField(null=True, blank=True,upload_to='static/image/announcement')
    logo_organization = models.ImageField(null=True, blank=True,upload_to='static/image/event_pic')
    announcement = models.ImageField(null=True, blank=True,upload_to='static/image/logo_organization')
    description = models.TextField(max_length=500, default="",editable=True)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    price = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-updated','created']

