from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
  """Base abstract model."""

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True
    ordering = ("-created_at",)


class User(BaseModel, AbstractUser):
  """Custom user model."""

  date_joined = None

  def __str__(self) -> str:
    """Return string representation of the user."""
    return f"{self.first_name} {self.last_name} <{self.email}>"
