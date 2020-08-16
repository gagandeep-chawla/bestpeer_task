from rest_framework import routers
from django.urls import path, include

from crud.views import TodoListViewSet

router = routers.DefaultRouter()
router.register('todolist', TodoListViewSet)

urlpatterns = [
        path('api/',include(router.urls))
]