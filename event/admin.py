from django.contrib import admin
from .models import Event,Topic, Participant, ParticipantType,CPD
# Register your models here.
admin.site.register(Event)
admin.site.register(Topic)
admin.site.register(Participant)
admin.site.register(ParticipantType)
admin.site.register(CPD)

