from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
