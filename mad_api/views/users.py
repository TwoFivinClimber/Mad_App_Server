'''Users module for request handeling'''

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import User, Interest, Category
from .interests import InterestSerializer

class UserView(ViewSet):
    '''User View'''
    def retrieve(self, request, pk):
        '''returns single user'''
        user = User.objects.get(pk=pk)
        
        interests = Interest.objects.filter(uid = user)
        interestst_serialized = InterestSerializer(interests, many=True)
        user.interests = interestst_serialized.data
        
        user_serialized = UserSerializer(user)
        
        return Response(user_serialized.data)
    
    def update(self, request, pk):
        '''updates the user and interests'''
        user = User.objects.get(pk=pk)
        
        user.name = request.data['name']
        user.image = request.data['image']
        user.tag = request.data['tag']
        user.location = request.data['location']
        user.lat = request.data['lat']
        user.long = request.data['long']
        user.age = request.data['age']
        user.save()

        interests = request.data['interests']
        
        existing_interests = Interest.objects.filter(uid = user)
        
        if existing_interests is not None:
            for interest in existing_interests:
                interest.delete()
        
        if interests is not None:
            for interest in interests:
                Interest.objects.create(uid = user, category = Category.objects.get(pk = interest))
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        '''Handels deletion of user'''
        user = User.objects.get(pk=pk)
        
        user.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'name', 'image', 'tag', 'location', 'lat', 'long', 'age', 'interests')
