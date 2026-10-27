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

def test_km_miles_normal():
    r = client.get("/conversion/km_miles", params={"km": 10})
    assert r.status_code == 200
    assert r.json()["miles"] == pytest.approx(6.21371)


def test_km_miles_limite():
    r = client.get("/conversion/km_miles", params={"km": 0})
    assert r.status_code == 200
    assert r.json()["miles"] == 0


def test_km_miles_erreur():
    r = client.get("/conversion/km_miles", params={"km": -5})
    assert r.status_code == 400