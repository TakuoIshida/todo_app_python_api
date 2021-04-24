import json
from http.client import PARTIAL_CONTENT

from django.db import models
from django_filters import filters
from rest_framework import response, serializers, status
from rest_framework.views import APIView

from .models import TodoModel
from .serializers import TodoSerializer


class TodoListFilter(filters.Filter):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')
    isDeleted = filters.BooleanFilter(lookup_expr=False)

    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoViewSet(APIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    filter_class = TodoListFilter

    def get(self, request):
        requestParams = request.query_params
        queryset = TodoModel.objects.all()
        serializer = TodoSerializer(instance=queryset, many=True)
        # filterset = TodoListFilter(
        #     requestParams, queryset=TodoModel.objects.all())
        ret = serializer.data
        data = {
            "ret": ret,
            "request": requestParams,
        }
        return response.Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        print(request)
        # todo_idの有無によって新規・更新を分ける
        param = request.data
        if param['todo_id'] == '' or param['todo_id'] == None:
            # 新規作成
            serializer = TodoSerializer(data=param)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = {
                "newSavedData": serializer.data
            }
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            # 更新
            try:
                todo = TodoModel.objects.get(pk=param.get('todo_id'))
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                # partial = true?
            serializer = TodoSerializer(instance=todo, data=param)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = {
                "savedData": serializer.data
            }
        return response.Response(data, status=status.HTTP_200_OK)
        # return response.Response(status=status.HTTP_200_OK)
