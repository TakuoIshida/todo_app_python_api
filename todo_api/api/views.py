import json

from django.db import models
from django_filters import fields, filters
from rest_framework import response, status, viewsets
from rest_framework.views import APIView

from .models import TodoModel
from .serializers import TodoSerializer


class TodoListFilter(filters.Filter):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')
    delete_flg = filters.BooleanFilter(lookup_expr=False)

    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoViewSet(APIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        requestParams = request.query_params
        data = {
            "article": "this is test",
            "request": requestParams,
        }
        return response.Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        param = json.loads(request.body)
        return response.Response(param, status=status.HTTP_200_OK)
