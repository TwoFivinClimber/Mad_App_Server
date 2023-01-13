from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mad_api.models import Category

class CategoryView(ViewSet):
    '''Category View'''
      
    def list(self, request):
      
        categories = Category.objects.all()
      
        categories_serialized = CategorySerializer(categories, many=True)
      
        return Response(categories_serialized.data)


class CategorySerializer(serializers.ModelSerializer):
    '''JSON serializer for categories'''
    class Meta:
        model = Category
        fields = ('id', 'name')
