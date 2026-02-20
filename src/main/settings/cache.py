from main.env import env

CACHES = {
  "default": {
    **env.cache(backend="django_redis.cache.RedisCache"),
    "OPTIONS": {
      "CLIENT_CLASS": "django_redis.client.DefaultClient",
    },
  }
}
