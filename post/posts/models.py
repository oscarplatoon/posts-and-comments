from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return f"ID: {self.id} \nTitle: {self.title}"

class Comment(models.Model):
    body = models.CharField(max_length=1024)
    post = models.ForeignKey(Post,
    on_delete=models.CASCADE,
    related_name='comments')

    def __str__(self) -> str:
        return f"ID: {self.id} \nOn Post: {self.post}\nText: {self.body[:60]}..."