from .views import CategoryList, ProductList
from django.urls import path

urlpatterns = [
    path('category',CategoryList.as_view()),
    path('product',ProductList.as_view()),

]
