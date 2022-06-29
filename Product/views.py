from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from rest_framework.generics import ListAPIView

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

