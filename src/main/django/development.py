from .base import *

INSTALLED_APPS.append("silk")
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
