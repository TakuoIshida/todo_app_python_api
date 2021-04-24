from django import urls
from django.urls import include, path

from .views import TodoViewSet

urlpatterns = [
    path('todos', TodoViewSet.as_view(), name="todo")
]
