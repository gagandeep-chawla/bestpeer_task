from rest_framework import routers, serializers, viewsets

from crud.models import TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= TodoList
        fields = '__all__'