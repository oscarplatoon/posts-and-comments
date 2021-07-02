from django.contrib import admin
from django.urls import path
from posts_app import views

# blog/posts/5

app_name = "posts_app"

urlpatterns = [
    path("posts/", views.index, name="post-list"),
    path("posts/<int:post_id>", views.post_detail, name="post-detail")
]
