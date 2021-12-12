from django.db import models

# Create your models here.
class Event(models.Model):
    nama = models.CharField(max_length=100)
    # tanggal = models.DateTimeField()
    # tempat = models.CharField(max_length=100)
    # hosted_by = models.CharField(max_length=100)
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

