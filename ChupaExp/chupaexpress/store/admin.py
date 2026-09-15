from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'createdAt')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_editable = ('name',)
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'category', 'createdAt')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    list_filter = ('category',)
    editable_fields = ('price', 'category')
    ordering = ('name')