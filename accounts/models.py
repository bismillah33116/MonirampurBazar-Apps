from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings

USER_ROLES = (
    ("customer", "Customer"),
    ("vendor", "Vendor"),
    ("admin","admin"),
)

    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default="customer")
    is_vendor = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

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


class CustomUser(AbstractUser):
    # এখানে extra fields যোগ করতে পারেন, যেমন:
    phone = models.CharField(max_length=15, blank=True)

    # groups & user_permissions conflict এড়াতে related_name দিন
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # unique name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set_permissions",  # unique name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
