from rest_framework.decorators import api_view
from rest_framework.response import Response
from mad_api.models import User


@api_view(['POST'])
def check_user(request):
    '''checks if user has created profile'''
    uid = request.data['uid']
    try :
        user = User.objects.get(uid = uid)
        data = {
          'id': user.id
        }
        return Response(data)
    except:
      data = { 'valid': False }

      return Response(data)
         
@api_view(['POST'])
def register_user(request):
    '''handels creation of new user'''
    user = User.objects.create(
      name=request.data['name'],
      image=request.data['image'],
      tag=request.data['tag'],
      location=request.data['location'],
      lat=request.data['lat'],
      long=request.data['long'],
      age=request.data['age']
    )
    
    data = {
      'id': user.id,
      'name': user.name,
    }
    
    return Response(data)
          
        
    
