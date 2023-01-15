from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Location, Event


class LocationView(ViewSet):
    '''handels requests for locations'''
      
    def list(self, request):

        location = Location.objects.get(event = request.query_params.get('event'))
        
        location_serialized = LocationSerializer(location)
        
        return Response(location_serialized.data, status.HTTP_200_OK)
        
    
    def create(self, request):
        '''handels create of location'''
        
        event = Event.objects.get(pk = request.data['event'])
        
        location = Location.objects.create(
          event = event,
          name = request.data['name'],
          type = request.data['type'],
          lat = request.data['lat'],
          long = request.data['long'],
          city = request.data['city'],
          state = request.data['state']
        )
        location.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        '''handels update of location'''
        location = Location.objects.get(pk=pk)
        
        location.name = request.data['name']
        location.type = request.data['type']
        location.lat = request.data['lat']
        location.long = request.data['long']
        location.city = request.data['city']
        location.state = request.data['state']
        location.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

          
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'event', 'name', 'type', 'lat', 'long', 'city', 'state')
    
