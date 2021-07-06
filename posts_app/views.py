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

def post_create(request):
    print(request.method)

    # POST request
    if request.method == "POST":

        try: 
            new_post = Post()
            new_post.title = request.POST["title"]
            new_post.body = request.POST["body"]
            new_post.name = request.POST["name"]
            new_post.save()
        except:
            print("ERRRRORRRRR!!!")

        return HttpResponse("Hey, you created a post!")

    ## GET request
    return render(request, "posts/post_create.html")


def post_update(request, post_id):
    print(request.method)
    post = Post.objects.get(id=post_id)

    # POST request
    if request.method == "POST":
        try: 
            
            post.title = request.POST["title"]
            post.body = request.POST["body"]
            post.name = request.POST["name"]
            post.save()
        except:
            print("ERRRRORRRRR!!!")

        return HttpResponse("Hey, you created a post!")

    ## GET request
    data = {
        "post": post
    }
    return render(request, "posts/post_update.html", data)

def post_delete(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponse("You successfully deleted this post.")
