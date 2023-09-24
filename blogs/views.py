from django.shortcuts import render
from rest_framework import generics
from .models import BlogsModel, Comment
from .serializers import BlogSerializer, CommentSerializer
# Create your views here.

class BlogListView(generics.ListCreateAPIView):
    queryset = BlogsModel.objects.all()
    serializer_class = BlogSerializer
    
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogsModel.objects.all()
    serializer_class = BlogSerializer

class CommentListView(generics.ListCreateAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer