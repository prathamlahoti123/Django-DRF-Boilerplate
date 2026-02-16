import secrets

from main.env import env

DJANGO_ADMIN_USERNAME = env.str("DJANGO_ADMIN_USERNAME")
DJANGO_ADMIN_EMAIL = env.str("DJANGO_ADMIN_EMAIL")
DJANGO_ADMIN_PASSWORD = env.str(
  "DJANGO_ADMIN_PASSWORD",
  default=secrets.token_urlsafe(10),
)
