from rest_framework import generics
from core.apps.products.models import Category, Product
from core.apps.products.serializers import CategorySerializer, ProductSerializer


# 1. Menu API: List categories that should be used as menus.
class MenuAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(use_as_menu=True)


# 2. Products List API: Return all products with nested images and variants.
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# 3. Products by Category API: Return products filtered by category name.
class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        return Product.objects.filter(category__name__iexact=category_name)
