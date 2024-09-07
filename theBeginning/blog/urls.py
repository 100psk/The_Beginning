from django.urls import path
from . import views

# Map the root URL to the 'blog_index' view
urlpatterns = [
    path('', views.blog_index, name='blog_index'), 
]