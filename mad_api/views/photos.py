from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Photo


class PhotoView(ViewSet):
    '''Photo type view'''
    
    def list(self, request):
        '''handels GET requests'''
        
        photos = Photo.objects.all()
        
        event = request.query_params.get('event')
        
        if event is not None:
            photos = photos.filter(event = event)
        
        photos_serialized = PhotoSerializer(photos, many=True)
        
        return Response(photos_serialized.data)
    
    def destroy(self, request, pk): 
        '''handels delete of photo'''
        photo = Photo.objects.get(pk=pk)
        photo.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url', 'event', 'public_id')
