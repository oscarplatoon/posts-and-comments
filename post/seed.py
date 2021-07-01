from posts.models import *

Post(title='First Post', body='Ipsum Lorem Deliciousness.').save()
Post(title='Second Post', body='Ipsum Lorem Tripped The Light Fantastic').save()
Post(title='Third Post', body='Lorem Ipsum Hocus Pocus').save()

Comment(body='I heard you like mudkips.', post=Post.objects.get(id=1)).save()
Comment(body='I put a comment on your post.', post=Post.objects.get(id=1)).save()
Comment(body="If it wasn't for my horse, I wouldn't have made it through college.", post=Post.objects.get(id=2)).save()
Comment(body='A staggering work of genius and intellect.', post=Post.objects.get(id=2)).save()
Comment(body="Tread carefully", post=Post.objects.get(id=3)).save()
Comment(body='And other filler text.', post=Post.objects.get(id=3)).save()
