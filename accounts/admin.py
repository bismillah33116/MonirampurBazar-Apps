from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import Profile, CustomUser

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.register(CustomUser, CustomUserAdmin)
