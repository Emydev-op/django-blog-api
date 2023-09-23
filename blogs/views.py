from django.shortcuts import render
from rest_framework import generics
from .models import BlogsModel
from .serializers import BlogSerializer
# Create your views here.

class BlogListView(generics.ListCreateAPIView):
    queryset = BlogsModel.objects.all()
    serializer_class = BlogSerializer
    
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogsModel.objects.all()
    serializer_class = BlogSerializer
