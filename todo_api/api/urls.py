from django import urls
from django.urls import path, include

from rest_framework import routers, urlpatterns

from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
urlpatterns = [
    path('', include(router.urls))
]
