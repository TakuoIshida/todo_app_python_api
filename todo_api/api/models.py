from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=400)
    delete_flg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
