import random
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Event, User, Category, Daytime, Photo
from .photos import PhotoSerializer


      
class EventView(ViewSet):
    '''Event type views'''
    
    def list(self, request):
        '''handels GET all request'''
        
        events = Event.objects.all()
        public = request.query_params.get('public')
        user = request.query_params.get('id')
        featured = request.query_params.get('featured')
        
        if public is not None and user is not None:
            events = events.filter(uid=user)
            events.filter(public = public)
            
        if public is not None:
            events = events.filter(public=public)
        
        if user is not None:
            events = events.filter(uid=user)
        
        if featured is not None:
            events = random.sample(list(events.filter(public=True)), 2)
        
        for event in events:
            photos = Photo.objects.filter(event=event)
            photos_serialized = PhotoSerializer(photos, many=True)
            event.photos = list(photos_serialized.data)
        
        events_serialized = EventSerializer(events, many=True)
        
        
        return Response(events_serialized.data)
    
    def retrieve(self, request, pk):
        '''handels GET single event'''
        
        event = Event.objects.get(pk=pk)
        
        photos = Photo.objects.filter(event=event)
        photos_serialized = PhotoSerializer(photos, many=True)
        return_photos = photos_serialized.data
        for photo in return_photos:
            photo['publicId'] = photo.pop('public_id')
        event.photos = list(return_photos)
        
        event_serialized = EventSerializer(event)
        
        return Response(event_serialized.data)
    
    def create(self, request):
        '''handels POST reques for event'''
        
        user = User.objects.get(pk=request.data['id'])
        category = Category.objects.get(pk=request.data['category'])
        daytime = Daytime.objects.get(pk=request.data['daytime'])
        photos = request.data['photos']
        
        
        event = Event.objects.create(
          title = request.data['title'],
          description = request.data['description'],
          date = request.data['date'],
          rating = request.data['rating'],
          public = request.data['public'],
          location = request.data['location'],
          city = request.data['city'],
          lat = request.data['lat'],
          long = request.data['long'],
          category = category,
          uid = user,
          daytime = daytime
        )
        
        if photos is not None:
            for obj in photos:
                photo = Photo(url = obj['url'], public_id = obj['publicId'], event=event)
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
        event.location = request.data['location']
        event.city = request.data['city']
        event.lat = request.data['lat']
        event.long = request.data['long']
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
                Photo.objects.create(url = photo['url'], public_id = photo['publicId'], event=event)
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        '''handels DELETE of event'''
        event = Event.objects.get(pk=pk)
        event.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'lat', 'long', 'city', 'date', 'rating', 'public', 'category', 'uid', 'daytime', 'photos')
        depth = 1
