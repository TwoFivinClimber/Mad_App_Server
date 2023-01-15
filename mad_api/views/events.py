from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Event, User, Category, Daytime, Photo

class EventView(ViewSet):
    '''Event type views'''
    
    def list(self, request):
        '''handels GET all request'''
        
        events = Event.objects.all()
        
        events_serialized = EventSerializer(events, many=True)
        
        return Response(events_serialized.data)
    
    def retrieve(self, request, pk):
        '''handels GET single event'''
        
        event = Event.objects.get(pk=pk)
        
        event_serialized = EventSerializer(event)
        
        return Response(event_serialized.data)
    
    def create(self, request):
        '''handels POST reques for event'''
        
        user = User.objects.get(uid=request.data['uid'])
        category = Category.objects.get(pk=request.data['category'])
        daytime = Daytime.objects.get(pk=request.data['daytime'])
        photo_urls = request.data['photos']
        
        event = Event.objects.create(
          title = request.data['title'],
          description = request.data['description'],
          date = request.data['date'],
          rating = request.data['rating'],
          public = request.data['public'],
          category = category,
          uid = user,
          daytime = daytime
        )
        
        if photo_urls is not None:
            for url in photo_urls:
                photo = Photo(url = url, event=event)
                photo.save()
        
        event_serialized = EventSerializer(event)
        
        return Response(event_serialized.data)
      
    def update(self, request, pk):
        '''handels update of events'''
        
        category = Category.objects.get(pk=request.data['category'])
        daytime = Daytime.objects.get(pk=request.data['daytime'])
        
        event = Event.objects.get(pk=pk)
        event.title = request.data['title']
        event.description = request.data['description']
        event.date = request.data['date']
        event.rating = request.data['rating']
        event.public = request.data['public']
        event.category = category
        event.daytime = daytime
        event.save()
        
        photo_urls = request.data['photos']
        existing_photos = list(Photo.objects.filter(event = event))
          
        if existing_photos is not None:
            for photo in existing_photos:
                photo.delete()
        
        if photo_urls is not None:
            for photo in photo_urls:
                Photo.objects.create(url = photo, event = event)
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        '''handels DELETE of event'''
        event = Event.objects.get(pk=pk)
        event.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'rating', 'public', 'category', 'uid', 'daytime')
        depth = 1
