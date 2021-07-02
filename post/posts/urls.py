from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    #/blog/
    path('', views.index, name='post-list'),

    #/posts/4
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
]
