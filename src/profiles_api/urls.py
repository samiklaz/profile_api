from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')
router.register('feed', UserProfileFeedViewSet)
# Base Name is not set for model view set, it automatically sets it on its own

urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='Hello View'),
    path('', include(router.urls))
]