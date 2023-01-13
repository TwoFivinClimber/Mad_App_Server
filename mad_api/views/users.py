'''Users module for request handeling'''

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mad_api.models import User

class UserView(ViewSet):
    '''User View'''
    def retrieve(self, request, pk):
        '''returns single user'''   
        user = User.objects.get(pk=pk)

        user_serialized = UserSerializer(user)
        
        return Response(user_serialized.data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'name', 'image', 'tag', 'location', 'lat', 'long', 'age')
