from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    #/posts/
    path('', views.index, name='index'),

    #/posts/4
    path('<int:post_id>/', views.detail, name='detail'),
]
