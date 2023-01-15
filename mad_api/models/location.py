'''Location Model'''
from django.db import models
from .event import Event



class Location(models.Model):
    '''location class'''
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
