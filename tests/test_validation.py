import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation import email_valide

client = TestClient(app)


def test_email_valide_normal():
    assert email_valide("nassira@hetic.net") is True


def test_email_valide_limite():
    assert email_valide("sans-arobase.fr") is False
    assert email_valide("a@b") is False
    assert email_valide("a..b@site.fr") is False


def test_email_valide_erreur():
    with pytest.raises(ValueError):
        email_valide("")


def test_route_email_valide_normal():
    reponse = client.get("/validation/email/nassira@hetic.net")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_email_valide_erreur():
    reponse = client.get("/validation/email/%20")
    assert reponse.status_code == 400
