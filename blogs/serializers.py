from rest_framework import serializers
from .models import BlogsModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsModel
        fields = '__all__'