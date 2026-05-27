from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'is_featured']
        
        read_only_fields = ['id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    post_detail = PostSerializer(source='post', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_detail', 'author', 'text']