from typing import TYPE_CHECKING

from django.conf import settings
from django.shortcuts import render
from drf_spectacular.utils import OpenApiExample, extend_schema, inline_serializer
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

if TYPE_CHECKING:
  from django.http import HttpResponse
  from rest_framework.request import Request


@extend_schema(
  responses={
    200: inline_serializer(
      name="HealthSerializer",
      fields={
        "response": serializers.CharField(),
      },
    ),
  },
  examples=[OpenApiExample("API Healthcheck", value={"response": "ok"})],
)
@api_view(["GET"])
def health(_: "Request") -> Response:
  """Healthcheck of the API."""
  body = {"response": "ok"}
  return Response(body, status=status.HTTP_200_OK)


@extend_schema(
  responses={
    200: inline_serializer(
      name="VersionSerializer",
      fields={
        "version": serializers.CharField(),
      },
    ),
  },
  examples=[OpenApiExample("API Version", value={"version": "0.0.1"})],
)
@api_view(["GET"])
def version(_: "Request") -> Response:
  """Version of the API."""
  body = {"version": settings.SPECTACULAR_SETTINGS["VERSION"]}
  return Response(body, status=status.HTTP_200_OK)


def index(request: "Request") -> "HttpResponse":
  """Display the index HTML page."""
  context = {"message": "Hello, World!"}
  return render(request, "index.html", context)
