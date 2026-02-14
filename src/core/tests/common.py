from functools import lru_cache

from django.test import TestCase
from faker import Faker
from rest_framework.test import APITestCase

from core.models import User


@lru_cache
def get_faker() -> Faker:
  """Return cached instance of Faker."""
  return Faker()


def create_user(faker: Faker) -> User:
  """Create and return a new user object using random user data."""
  return User.objects.create_user(
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
