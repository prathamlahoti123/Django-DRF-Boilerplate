import os

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
  SpectacularAPIView,
  SpectacularRedocView,
  SpectacularSwaggerView,
)

from .constants import DjangoSettingsModule

urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
  path(
    "api/schema/docs/",
    SpectacularSwaggerView.as_view(url_name="schema"),
    name="docs",
  ),
  path(
    "api/schema/redoc/",
    SpectacularRedocView.as_view(url_name="schema"),
    name="redoc",
  ),
  path("", include("core.urls")),
]

if os.environ["DJANGO_SETTINGS_MODULE"] == DjangoSettingsModule.DEVELOPMENT:
  urlpatterns += [
    path("silk/", include("silk.urls", namespace="silk")),
  ]
