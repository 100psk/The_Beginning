# Create your models here.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Field for the post title
    content = models.TextField()              # Field for the post content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when the post was last updated

    def __str__(self):
        return self.title
