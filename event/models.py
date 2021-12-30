from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(null=True,max_length=100)
    code = models.CharField(max_length=100,default='')
    event_website = models.CharField(max_length=200,blank=True) 
    no_rek = models.TextField(max_length=500,default='',editable=True,blank=True,null=True)
    organized_by = models.CharField(max_length=100)
    hosted_by = models.CharField(max_length=100)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    place = models.CharField(max_length=100)
    event_pict= models.ImageField(null=True, blank=True,upload_to='event_pict/')
    logo_organization = models.ImageField(null=True, blank=True,upload_to='logo_organization/')
    announcement = models.ImageField(null=True, blank=True,upload_to='announcement/')
    description = models.TextField(max_length=500, default="",editable=True,blank=True,null=True)
    status = models.BooleanField(default=False)
    free_event = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class CPD(models.Model):
    name = models.CharField(max_length=200)
    # workshop_type = models.
    # register_type= 
    quota = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    venue = models.CharField(max_length=200)
    price = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ParticipantType(models.Model):
    category_name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Participant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    # Generator
    code_registration = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField(null=False,blank=False,unique=True)
    paid = models.BooleanField(default=False)
    type = models.ForeignKey(ParticipantType,on_delete=models.SET_NULL,null=True)
    bill = models.ImageField(null=True,blank=True,upload_to='participant/{}/'.format(code_registration))
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.event.name + '--'+self.user.name

class Symposium(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

class Price(models.Model):
    participant = models.ForeignKey(Symposium,on_delete=models.CASCADE)
    price = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    certificate_format = models.ImageField(null=True,blank=True,upload_to='certificate/')
    certificate_back = models.ImageField(null=True,blank=True,upload_to='certificate/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
