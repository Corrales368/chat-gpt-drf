from rest_framework import viewsets
from apps.products.models import Product
from apps.products.api.serializers import ProductSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer