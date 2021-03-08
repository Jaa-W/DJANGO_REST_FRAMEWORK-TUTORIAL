from django import template
from django.db.models.query import QuerySet
from rest_framework import permissions, viewsets
from posts.models import Post
from django.contrib.auth.models import User
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render
from .templates import *

@api_view()
def home_page(request):
    data = {'posts': Post.objects.reverse()[0:5]}
    return render(request, 'home_page.html', data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # un-authetcated only read 

    def perform_create(self, serializer):                       # Adding information about user to created post
        serializer.save(owner = self.request.user)
    
    def retrieve(self, request, pk=None):
        post_data =Post.objects.get(id = pk)
        data = {'post': post_data}
        return render(request, 'post_detail.html', data)
