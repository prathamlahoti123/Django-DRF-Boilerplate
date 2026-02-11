from main.env import env

REST_FRAMEWORK = {
  "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
  "TITLE": env.str("OPENAPI_TITLE", "Set OpenAPI Title"),
  "DESCRIPTION": env.str("OPENAPI_DESCRIPTION", "Set OpenAPI Description"),
  "VERSION": env.str("OPENAPI_VERSION", "0.0.1"),
  "COMPONENT_SPLIT_REQUEST": True,
  "SERVE_INCLUDE_SCHEMA": False,
}
