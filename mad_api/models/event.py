'''Event Model'''

from django.db import models
from .user import User
from .category import Category
from .daytime import Daytime

class Event(models.Model):
    '''Event class'''
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=75)
    lat = models.FloatField(null=True, default=None)
    long = models.FloatField(null=True, default=None)
    city = models.CharField(max_length=75)
    date = models.DateField()
    daytime = models.ForeignKey(Daytime, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    public = models.BooleanField()
    
    @property
    def photos(self):
        '''will be used to return photos of event'''
        return self.__photos

    @photos.setter
    def photos(self, value):
        self.__photos=value
    