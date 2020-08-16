from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.response import Response

from crud.serializers import TodoListSerializer
from crud.models import TodoList

# Create your views here.

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def delete(self, request, pk=None):
        instance = TodoList.objects.get(id = pk)
        instance.delete()   