from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())
    
    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    @property
    def subtotal(self):
        return self.product.price * self.quantity