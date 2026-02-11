from functools import lru_cache
from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker
from rest_framework.test import APITestCase

if TYPE_CHECKING:
  from django.contrib.auth.models import User


@lru_cache
def get_faker() -> Faker:
  """Return cached instance of Faker."""
  return Faker()


def create_user(faker: Faker) -> "User":
  """Create and return a new user object using random user data."""
  user = get_user_model()
  return user.objects.create_user(
    username=faker.user_name(),
    email=faker.email(),
    password=faker.password(),
  )


class BaseTestCase(TestCase):
  """Base TestCase-based class, providing some useful objects for each test."""

  def setUp(self) -> None:
    """Initialize reusable objects for each test."""
    self.faker = get_faker()


class BaseAPITestCase(APITestCase):
  """Base class to sub APITestCase, providing some useful objects for each test."""

  def setUp(self) -> None:
    """Initialize reusable objects for each test."""
    self.faker = get_faker()
