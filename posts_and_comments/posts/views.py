from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .util import get_post_by_id

# Create your views here.


def index(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)


def post(request, id):
    current_post = get_post_by_id(id)
    context = {'current_post': current_post}
    return render(request, 'posts/post.html', context)
