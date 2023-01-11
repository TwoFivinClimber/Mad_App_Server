"""interest Model"""

from django.db import models
from .category import Category
from .user import User

class Interest(models.Model):
    '''Interest class'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
