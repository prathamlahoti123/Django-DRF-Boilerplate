from io import StringIO

from django.core.management import call_command
from django.test import override_settings

from core.models import User
from core.tests.common import BaseTestCase, create_user


class TestCreateSUCommand(BaseTestCase):
  """Tests for createsu management command."""

  def test_create_superuser(self) -> None:
    output = StringIO()
    username = self.faker.user_name()
    email = self.faker.email()
    password = self.faker.password()

    with override_settings(
      DJANGO_ADMIN_USERNAME=username,
      DJANGO_ADMIN_EMAIL=email,
      DJANGO_ADMIN_PASSWORD=password,
    ):
      call_command("createsu", stdout=output, no_color=True)

    user = User.objects.get(username=username)
    assert user.email == email
    assert user.is_superuser is True
    assert user.is_staff is True
    assert user.check_password(password) is True
    assert f"Created superuser. Password: {password}" in output.getvalue()

  def test_user_already_exists(self) -> None:
    output = StringIO()
    existing_user = create_user(self.faker)
    user_count_before = User.objects.count()

    with override_settings(
      DJANGO_ADMIN_USERNAME=existing_user.username,
      DJANGO_ADMIN_EMAIL=self.faker.email(),
      DJANGO_ADMIN_PASSWORD=self.faker.password(),
    ):
      call_command("createsu", stdout=output, no_color=True)

    assert User.objects.count() == user_count_before
    assert "User already exists." in output.getvalue()
