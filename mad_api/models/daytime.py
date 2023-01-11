'''Daytime Model'''

from django.db import models

class Daytime(models.Model):
    '''Daytime class'''
    name = models.CharField(max_length=50)
  