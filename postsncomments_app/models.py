from django.db import models
from django.db.models.fields import CharField

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1800)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=1800)
