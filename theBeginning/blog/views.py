from django.shortcuts import render

# Dette bliver vist, når siden kaldes
def blog_index(request):
    return render(request, 'blog/index.html')