from django.urls import path

from .views import TodoViewSet

# TODO: テスト工藤開発時に以下のURLパターンにして、各メソッドごとにテストをする
# https://qiita.com/murapon/items/8a6a1715712ddd1a4ac1
urlpatterns = [
    path('todos', TodoViewSet.as_view(), name="todo")
]
