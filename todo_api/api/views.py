from django_filters import rest_framework as filters
from rest_framework import response, status
from rest_framework.views import APIView

from .models import TodoModel
from .serializers import TodoSerializer


class TodoListFilter(filters.FilterSet):
    title = filters.filters.CharFilter(lookup_expr='icontains')
    content = filters.filters.CharFilter(lookup_expr='icontains')
    isDeleted = filters.filters.BooleanFilter(lookup_expr=False)

    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoViewSet(APIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    filter_class = TodoListFilter

    def get(self, request):
        requestParams = request.query_params
        # params = {
        #     'isDeleted': requestParams.get('isDeleted')
        # }
        # TODO: 検索機能
        qs = TodoModel.objects.filter(isDeleted=False)
        # filterset = TodoListFilter(
        #     params, queryset=qs)
        serializer = TodoSerializer(instance=qs, many=True)
        data = {
            "status": status.HTTP_200_OK,
            "message": "",
            "result": serializer.data,
        }
        return response.Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        # idの有無によって新規・更新を分ける
        param = request.data
        if param['id'] == '' or param['id'] == None:
            # if True:
            # 新規作成
            serializer = TodoSerializer(data=param)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = {
                "status": status.HTTP_200_OK,
                "message": "",
                "result": serializer.data,
            }
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            # 更新
            try:
                todo = TodoModel.objects.get(pk=param.get('id'))
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
                "status": status.HTTP_200_OK,
                "message": "",
                "result": serializer.data,
            }
        return response.Response(data, status=status.HTTP_200_OK)
