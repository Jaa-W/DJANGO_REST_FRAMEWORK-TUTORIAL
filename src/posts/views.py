from rest_framework import  generics, permissions, viewsets
from posts.models import Post
from django.contrib.auth.models import User
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # un-authetcated only read 

    def perform_create(self, serializer):                       # Adding information about user to created post
        serializer.save(owner = self.request.user)
