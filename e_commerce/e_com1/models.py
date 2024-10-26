from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models





class Product(models.Model):
    
    PRODUCT_TYPES = [
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Meat', 'Meat'),
    ('Bread', 'Bread')]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    product_type = models.CharField(max_length=10, null=True, blank=True,choices=PRODUCT_TYPES)

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.user}'s cart"
