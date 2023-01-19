'''Model for User'''

from django.db import models


class User(models.Model):
    '''User Class'''
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    tag = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    age = models.IntegerField()

    @property
    def interests(self):
        '''used to return users interests'''
        return self.__interests

    @interests.setter
    def interests(self, value):
        self.__interests=value
