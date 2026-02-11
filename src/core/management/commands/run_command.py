from typing import Any

from django.core.management.base import BaseCommand


class Command(BaseCommand):
  """Custom arbitrary command."""

  def handle(self, *args: Any, **options: Any) -> None:  # noqa: ARG002
    """Logic to be executed by the command."""
    self.stdout.write("Hello, World!")
