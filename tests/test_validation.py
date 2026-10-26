import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation import email_valide, mdp_robuste

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


def test_mdp_robuste_normal():
    assert mdp_robuste("Abcdef1!") is True


def test_mdp_robuste_limite():
    assert mdp_robuste("Abcde1!") is False  # 7 caractères
    assert mdp_robuste("abcdefg1!") is False  # pas de majuscule
    assert mdp_robuste("ABCDEFG1!") is False  # pas de minuscule
    assert mdp_robuste("Abcdefgh!") is False  # pas de chiffre
    assert mdp_robuste("Abcdefg12") is False  # pas de caractère spécial


def test_mdp_robuste_erreur():
    with pytest.raises(ValueError):
        mdp_robuste("")


def test_route_mdp_robuste_normal():
    reponse = client.get("/validation/mdp/Abcdef1!")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_mdp_robuste_erreur():
    reponse = client.get("/validation/mdp/%20")
    assert reponse.status_code == 400
