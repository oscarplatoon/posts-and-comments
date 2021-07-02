from django.shortcuts import render
from django.http import HttpResponse
from posts_app.models import Post

def index(request):
    stuff = {
        "posts": Post.objects.all()
    }
    return render(request, "posts/index.html", stuff)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if post == None:
        HttpResponse("HEY, that post doesn't exist!")

    stuff = {
        "post": Post.objects.get(id=post_id)
    }
    return render(request, "posts/post_detail.html", stuff)
