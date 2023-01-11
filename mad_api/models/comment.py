'''Comment Model'''

from django.db import models
from .user import User
from .event import Event

class Comment(models.Model):
    '''Comment Class'''
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    
    