from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mad_api.models import Interest, User

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
  

class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'category', 'uid')
