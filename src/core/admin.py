from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
  """Custom admin for User model using django-unfold package."""
