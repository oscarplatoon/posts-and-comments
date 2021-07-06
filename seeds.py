from posts_app.models import *

Post.objects.all().delete()

p1 = Post(title="My first post", body="Blah", name="Ankur")
p1.save()