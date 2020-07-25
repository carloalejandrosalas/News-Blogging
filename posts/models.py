from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=100)    
    content = models.TextField()
    registered_at = models.DateTimeField(auto_now=True)