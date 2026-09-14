from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    descrption = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    # Override the save method to automatically generate a slug from the name if it is not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    # Define a method to get the absolute URL for the category detail page
    def get_absolute_url(self):
        return reverse('store:category_detail', args=[self.slug])

    def __str__(self):
        return self.name


# class of products
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True) # no duplicates allowed
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True) # nullable description
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    createdAt = models.DateTimeField(auto_now_add=True)

    # Override the save method to automatically generate a slug from the name if it is not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # Define a method to get the absolute URL for the product detail page
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    # dunder method to return the name of the product when the object is printed
    def __str__(self):
        return self.name
    