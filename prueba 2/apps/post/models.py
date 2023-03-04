from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title