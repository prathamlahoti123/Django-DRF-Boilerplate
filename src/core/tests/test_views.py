from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCoreViews(APITestCase):
  """Tests views of the core app."""

  def test_health(self) -> None:
    url = reverse("health")
    resp = self.client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data.get("response") == "ok"

  def test_version(self) -> None:
    url = reverse("version")
    resp = self.client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data.get("version") == settings.SPECTACULAR_SETTINGS["VERSION"]

  def test_index(self) -> None:
    url = reverse("index")
    resp = self.client.get(url)
    assert resp.status_code == status.HTTP_200_OK
