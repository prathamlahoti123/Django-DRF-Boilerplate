from main.env import env

from .base import *

DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

INSTALLED_APPS.append("silk")
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
