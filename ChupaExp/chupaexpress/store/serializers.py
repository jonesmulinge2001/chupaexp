from rest_framework import serializers
from .models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'descrption', 'createdAt']
        read_only_fields = ['id', 'slug', 'createdAt']

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'category', 'createdAt']
        read_only_fields = ['id', 'slug', 'createdAt']

