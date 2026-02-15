from main.env import env

UNFOLD = {
  "SITE_TITLE": env.str("UNFOLD_SITE_TITLE", "Django Admin Title"),
  "SITE_HEADER": env.str("UNFOLD_SITE_HEADER", "Django Admin Header"),
}
