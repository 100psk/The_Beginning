from django.shortcuts import render
from .models import Post

# Dette bliver vist, når siden kaldes
def blog_index(request):
    posts = Post.objects.all()
    return render(request, 'templates/blog/index.html', {'posts: posts'})
