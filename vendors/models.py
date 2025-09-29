from django.db import models
from accounts.models import VendorProfile


class Vendor(models.Model):
    profile = models.OneToOneField(VendorProfile, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)


def __str__(self):
    return self.profile.shop_name