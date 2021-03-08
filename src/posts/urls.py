from django.urls import path
from django.urls.conf import include
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Creating router
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)


# URLS
urlpatterns = ([
    path('',views.home_page),
    path('', include(router.urls)),
])
urlpatterns+=staticfiles_urlpatterns()
