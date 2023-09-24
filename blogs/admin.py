from django.contrib import admin
from .models import BlogsModel, Comment
# Register your models here.

admin.site.register(BlogsModel)
admin.site.register(Comment)