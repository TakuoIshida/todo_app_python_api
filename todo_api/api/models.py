from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    delete_flg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
