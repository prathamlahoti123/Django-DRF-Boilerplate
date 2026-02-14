from .base import *

INSTALLED_APPS.extend(
  [
    "silk",
    "debug_toolbar",
    "django_extensions",
  ]
)

INTERNAL_IPS = ["127.0.0.1"]

# DebugToolbarMiddleware should be placed as early as possible
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
