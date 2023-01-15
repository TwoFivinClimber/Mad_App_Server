from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mad_api.models import Daytime

class DaytimeView(ViewSet):
    '''Daytime class'''
    
    def list(self, request):

        daytimes = Daytime.objects.all()
        
        daytimes_serialized = DaytimeSerializer(daytimes, many=True)

        
        return Response(daytimes_serialized.data)
    
    
    
class DaytimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Daytime
        fields = ('id', 'name')
        