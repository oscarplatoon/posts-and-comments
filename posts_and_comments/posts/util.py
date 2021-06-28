from .models import Post, Comment


def get_post_by_id(post_id):
    return Post.objects.get(id=post_id)