from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#for adding product
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    image = models.ImageField(upload_to='product_pic/', blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())