from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Interest, User, Category

class InterestView(ViewSet):
    '''User Interest Views'''
  
    def list(self, request):
        '''handels GET interests by user'''
        interests = Interest.objects.all()
        
        user = User.objects.get(pk = request.data['id'])
      
        if user is not None:
          
            user_interests=(interests.filter(uid = user.id))
          
          
        serialized = InterestSerializer(user_interests, many=True)
      
        return Response(serialized.data)
      
    def create(self, request):
        '''handels creation of user interests'''
        
        user = User.objects.get(pk=request.data['uid'])
        interests = request.data['interests']
        
        existing_interests = Interest.objects.filter(uid = user)
        
        if existing_interests is not None:
            for interest in existing_interests:
                interest.delete()
        
        if interests is not None:
            for category in interests:
              
                Interest.objects.create(category=Category.objects.get(pk=category), uid=user)
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'category', 'uid')
