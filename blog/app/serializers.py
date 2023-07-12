from django.contrib.auth.models import User
from rest_framework import serializers

from blog.app.models import Article, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    key = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Comment
        fields = ['key', 'author', 'created_at', 'updated_at', 'content']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'created_at', 'updated_at', 'title', 'content', 'comments']
