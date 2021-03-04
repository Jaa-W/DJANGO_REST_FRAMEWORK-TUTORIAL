from rest_framework import  generics, permissions
from posts.models import Post
from django.contrib.auth.models import User
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, UserSerializer

class UserList(generics.ListAPIView):                           # SHOW ALL USERS
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):                     # SHOW USER DETAILS
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class PostList(generics.ListCreateAPIView):                     # SHOW ALL POSTS
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # un-authetcated only read 

    def perform_create(self, serializer):                       # Adding information about user to created post
        serializer.save(owner = self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):        # SHOW POST DETAILS
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    # un-authetcated only read 