from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogsModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogsModel, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title + " | " + self.author.username