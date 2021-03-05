from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

# Settings views from ViewSet
post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = views.UserViewSet.as_view({'get': 'list'})
user_detail = views.UserViewSet.as_view({'get': 'retrieve'})

# URLS
urlpatterns = format_suffix_patterns([
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('', views.api_root)
])
