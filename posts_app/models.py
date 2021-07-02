from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    name = models.CharField(max_length=32)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.CharField(max_length=128)
    name = models.CharField(max_length=32)
