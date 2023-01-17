from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mad_api.models import Comment, Event, User

class CommentView(ViewSet):
    '''comments view'''
    
    def list(self, request):
        'handels comments by event'
        comments = Comment.objects.filter(event = request.query_params.get('event', None))
        
        comments_serialized = CommentSerializer(comments, many=True)
        
    
        return Response(comments_serialized.data)
      
    def create(self, request):
        '''handels create of comments'''
        event = Event.objects.get(pk = request.data['event'])
        user = User.objects.get(pk = request.data['user'])

        comment = Comment.objects.create(
          date = datetime.now().date(),
          content = request.data['content'],
          event = event,
          uid = user
        )
        comment.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        '''handels update comment'''
        
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data['content']
        comment.edited = datetime.now().date()
        comment.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      
    def delete(self, request, pk):
        '''handels deletion of comments'''
        
        comment = Comment.objects.get(pk=pk)
        
        comment.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
          
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'date', 'content', 'event', 'uid')
        depth = 1
        