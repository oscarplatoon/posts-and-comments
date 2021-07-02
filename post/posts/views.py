from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post, Comment

def get_post(post_id):
    return Post.objects.get(id=post_id)

def get_all_posts():
    return Post.objects.all()

def index(request):
    post_list = get_all_posts()
    post_data = {'posts':post_list}
    return render(request, 'posts/index.html', post_data)

def detail(request, post_id):
    post = get_post(post_id)
    try:
        post_comments = post.comments.all()
    except(KeyError, Comment.DoesNotExist):
        return render(request,
        'posts/detail.html',
        {
            'post':post,
            'error_message' : "This post has no comments."
        })
    else:
        return render(request,
        'posts/detail.html',
        post_comments)