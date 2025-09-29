from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to='vendor_logos/', blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.0) # percentage


    def __str__(self):
        return self.shop_name