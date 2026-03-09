import socket
from typing import TYPE_CHECKING

from django.conf import settings

if TYPE_CHECKING:
  from django.http import HttpRequest


INTERNAL_IPS = [
  "127.0.0.1",
  socket.gethostbyname(socket.gethostname())[:-1] + "5",
]


def show_toolbar(request: "HttpRequest") -> bool:
  """Whether to show the debug toolbar or not.

  NOTE: this callback is required to be set for DEBUG_TOOLBAR_CONFIG setting
        when running the application in Docker.
  """
  return settings.DEBUG and request.META.get("REMOTE_ADDR") in INTERNAL_IPS


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}
