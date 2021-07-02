from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, INDEX route is working!!!")
    

def post_detail(request, post_id):
    return HttpResponse(f"Hey, POST_DETAIL for item {post_id} route is working!!!")
