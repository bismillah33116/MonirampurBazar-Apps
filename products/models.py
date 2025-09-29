from django.db import models
from django.conf import settings
from vendors.models import Vendor


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    vendor = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    images = models.ImageField(upload_to='products/', blank=True, null=True)

    # এই লাইন যোগ করুন
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


