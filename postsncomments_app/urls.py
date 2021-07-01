from django import urls
from django.urls import path
from . import views
import postsncomments_app


app_name = "postsncomments_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('/posts/<int:post_id>/', views.posts, name="posts"),
]