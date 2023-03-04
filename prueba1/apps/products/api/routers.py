from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('api/v1/products', views.ProductModelViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]