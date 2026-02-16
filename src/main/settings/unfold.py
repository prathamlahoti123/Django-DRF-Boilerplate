from main.env import env

UNFOLD = {
  "SITE_TITLE": env.str("DJANGO_ADMIN_UI_TITLE", "Django Admin Title"),
  "SITE_HEADER": env.str("DJANGO_ADMIN_UI_HEADER", "Django Admin Header"),
}
