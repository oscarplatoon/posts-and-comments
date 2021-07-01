from django.shortcuts import render
from .models import *

def index(request):
    post_list = Post.objects.all
    print(post_list)
    data = { 'post_list': post_list}
    return render(request, 'postsncomments_app/index.html', data)
    

def posts(request, post_id):
    post = Post.objects.get(id = post_id)
    data = {'post': post}
    return render(request, 'postsncomments_app/posts.html', data)