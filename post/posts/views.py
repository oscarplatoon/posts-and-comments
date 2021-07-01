from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def detail(request, post_id):
    return HttpResponse(f"You're looking at post {post_id}.")