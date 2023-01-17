from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from mad_api.models import Category

class CategoryView(ViewSet):
    '''Category View'''
      
    def list(self, request):
        '''returns ctaegories formatted for react select menu'''
        categories = Category.objects.all()
      
        categories_serialized = CategorySerializer(categories, many=True)
        
        for category in categories_serialized.data:
            category['value'] = category.pop('id')
            category['label'] = category.pop('name')
      
        return Response(categories_serialized.data)


class CategorySerializer(serializers.ModelSerializer):
    '''JSON serializer for categories'''
    class Meta:
        model = Category
        fields = ('id', 'name')
