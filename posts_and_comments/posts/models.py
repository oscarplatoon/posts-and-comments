from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=600)


class Comment(models.Model):
    body = models.CharField(max_length=300)
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
