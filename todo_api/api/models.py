from django.db import models


class TodoModel(models.Model):
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(max_length=400, null=False)
    isDeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
=======
    delete_flg = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
>>>>>>> master
