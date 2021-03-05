from django.urls import path
from django.urls.conf import include
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# Creating router
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)


# URLS
urlpatterns = ([
    path('', include(router.urls)),
])
