from django.shortcuts import render
from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from posts.serializers import PostSerializer

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *arg, **kwargs):                # SHOW ALL POST
        return self.list(request, *arg, **kwargs)

    def post(self, request, *arg, **kwargs):               # CREATE NEW POST                          
        return self.create(request, *arg, **kwargs)




class PostDetail(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *arg, **kwargs):                # SHOW POST DETAILS
        return self.retrieve(request, *arg, **kwargs)                           
        
    def put(self, request, *arg, **kwargs):                # EDIT POST
        return self.update(request, *arg, **kwargs)

    def delate(self, request, *arg, **kwargs):                # DELETE POST
        return self.destroy(request, *arg, **kwargs)
