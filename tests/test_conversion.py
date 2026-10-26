import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
URL = "/conversion/celsius_fahrenheit"


def test_celsius_normal():
    r = client.get(URL, params={"celsius": 100})
    assert r.status_code == 200
    assert r.json()["fahrenheit"] == 212


def test_celsius_limite():
    r = client.get(URL, params={"celsius": -273.15})
    assert r.status_code == 200
    assert r.json()["fahrenheit"] == pytest.approx(-459.67)


def test_celsius_erreur():
    r = client.get(URL, params={"celsius": -300})
    assert r.status_code == 400