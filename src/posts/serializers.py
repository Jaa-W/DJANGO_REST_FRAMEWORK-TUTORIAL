from django.db import models
from rest_framework import fields, serializers
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many = True, read_only = True, view_name='post-detail')          # many beacouse users could have many posts
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = User
        fields = ['url','id', 'username', 'posts', 'owner']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Post
        fields = ['url','owner', 'id', 'title', 'content', 'author']
    # class Meta replaced that actions
    # id = serializers.IntegerField(read_only = True)
    # title = serializers.CharField(required = True, allow_blank = False, max_length = 100)
    # content = serializers.CharField(style ={'base_template': 'textarea.html'})
    # author = serializers.CharField(required = True, allow_blank = False, max_length = 100)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
        
