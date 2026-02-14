from .base import *

INSTALLED_APPS.extend(
  [
    "silk",
    "debug_toolbar",
  ]
)

INTERNAL_IPS = ["127.0.0.1"]

# SilkyMiddleware can be simply appended to the list of middlewares
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")

# DebugToolbarMiddleware should be as early as possible in the list of middlewares
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
