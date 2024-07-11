from django.db import models

class User(models.Model):
    # フィールドの定義例
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
