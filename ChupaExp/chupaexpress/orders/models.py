from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Order(models.Model):
    STATUS_CHIOCES = [
        ('pending', 'pending'),
        ('shipped', 'shipped'),
        ('deliverd', 'delivered'),
        ('cancelled', 'cancelled')
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHIOCES, default='pending')
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        pass

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity