from django.db import models

# Create your models here.
class BlogsModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title