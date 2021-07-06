from django.contrib import admin
from django.urls import path
from posts_app import views

# blog/posts/5

app_name = "posts_app"

urlpatterns = [
    path("posts/", views.index, name="post-list"),
    path("posts/<int:post_id>", views.post_detail, name="post-detail"),
    path("posts/<int:post_id>/update", views.post_update, name="post-update"),
    path("posts/<int:post_id>/delete", views.post_delete, name="post-delete"),
    path("posts/new", views.post_create, name="post-create")
]
