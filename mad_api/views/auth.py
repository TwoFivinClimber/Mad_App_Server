from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from mad_api.models import User, Interest, Category


@api_view(['POST'])
def check_user(request):
    '''checks if user has created profile'''
    uid = request.data['uid']
    try :
        user = User.objects.get(uid = uid)
        data = {
          'id': user.id,
          'uid': uid,
          'name': user.name,
          'image': user.image,
          'tag': user.tag,
          'location': user.location,
          'lat': user.lat,
          'long': user.long,
          'age': user.age
        }
        return Response(data)
    except:
        data = { 'valid': False }
        return Response(data)
         
@api_view(['POST'])
def register_user(request):
    '''handels creation of new user'''
    
    user = User.objects.create(
      uid=request.data['uid'],
      name=request.data['name'],
      image=request.data['image'],
      tag=request.data['tag'],
      location=request.data['location'],
      lat=request.data['lat'],
      long=request.data['long'],
      age=request.data['age']
    )
    
    interests = request.data['interests']
    
    if interests is not None:
        for interest in interests:
            Interest.objects.create(uid = User.objects.get(uid=user.uid), category= Category.objects.get(pk = interest))
        
    
    data = {
      'id': user.id,
      'name': user.name,
    }
    
    return Response(data)
          
        
    
