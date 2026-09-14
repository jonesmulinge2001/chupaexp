from django.shortcuts import render
from django_rest_framework import generics
from django_rest_framework .permissions import allowAny
from django_rest_framework import viewsets
fronm .models import Category, Product

# Create your views here.
# read only views for the store app

class CatgeroryListView(generics.ListAPIView): # generic view for listing all categories
    queryset = Category.objects.all() # returns all categories
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProductListView(generics.ListAPIView): # generic view for listing all products
    queryset = Product.objects.all() # returns all products
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = Product.objects.filter(available=True) # filter products by available field
        category_slug = self.kwargs.get('category_slug')
        search = self.request.query_params.get('search')
        if category_slug:
            qs = qs.filter(category__slug=category_slug) # filter products by category slug
        if search:
            qs = qs.filter(name__icontains=search)
        return qs

class CategoryDetailView(generics.RetrieveAPIView): # generic view for retrieving a single category
    queryset = Category.objects.all() # returns all categories
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug' # lookup field is the slug field

class ProductDetailView(generics.RetrieveAPIView): # generic view for retrieving a single product
    queryset = Product.objects.all() # returns all products
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug' # lookup field is the slug field