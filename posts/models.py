from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post:
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
