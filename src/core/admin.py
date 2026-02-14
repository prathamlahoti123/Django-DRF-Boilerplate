from django.contrib import admin
from unfold.admin import ModelAdmin  # type: ignore[import-untyped]

from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):  # type: ignore[misc]
  """Custom admin for User model using django-unfold package."""
