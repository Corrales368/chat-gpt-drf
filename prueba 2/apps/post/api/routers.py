from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('', views.PostModelViewSet, basename='post')


urlpatterns = [
    path('api/v1/posts', include(router.urls))
]