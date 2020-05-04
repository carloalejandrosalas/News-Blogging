from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=40)
    subtitle = models.TextField(max_length=40)
    cover_image = models.TextField()    
    content = models.TextField()
    registered_at = models.DateTimeField(auto_now=True)