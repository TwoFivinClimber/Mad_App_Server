'''Photo Model'''

from django.db import models
from .event import Event

class Photo(models.Model):
    '''Photo class'''
    url = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=75)
