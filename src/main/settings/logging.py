from main.env import env

LOG_LEVEL = env.str("DJANGO_LOG_LEVEL", default="INFO").upper()
LOGGING = {
  "version": 1,
  "disable_existing_loggers": False,
  "handlers": {
    "console": {
      "class": "logging.StreamHandler",
      "level": LOG_LEVEL,
      "formatter": "simple",
    },
  },
  "loggers": {
    "": {
      "handlers": ["console"],
      "level": LOG_LEVEL,
    },
  },
  "formatters": {
    "simple": {
      "format": "{asctime} {levelname} {message}",
      "style": "{",
    },
    "verbose": {
      "format": "{asctime} {levelname} - {name}.{module}.py (line {lineno:d}). {message}",  # noqa: E501
      "style": "{",
    },
  },
}
