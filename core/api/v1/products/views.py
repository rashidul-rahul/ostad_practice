from rest_framework import generics, filters
from core.apps.products.models import Category, Product
from rest_framework.pagination import PageNumberPagination
from core.apps.products.serializers import CategorySerializer, ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MenuAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(use_as_menu=True)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['name']


class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        return Product.objects.filter(category__name__iexact=category_name)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
