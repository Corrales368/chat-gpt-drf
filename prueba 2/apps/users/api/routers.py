from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('', views.UserModelViewSet, basename='users')


urlpatterns = [
    path('api/v1/users', include(router.urls))
]