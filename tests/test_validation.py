import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation import code_postal, email_valide, mdp_robuste

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
    reponse = client.get("/validation/email_valide/nassira@hetic.net")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_email_valide_erreur():
    reponse = client.get("/validation/email_valide/%20")
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
    reponse = client.get("/validation/mdp_robuste", params={"mdp": "Abcdef1!"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_mdp_robuste_avec_slash():
    reponse = client.get("/validation/mdp_robuste", params={"mdp": "Abc/def1!"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_mdp_robuste_erreur():
    reponse = client.get("/validation/mdp_robuste", params={"mdp": " "})
    assert reponse.status_code == 400


def test_code_postal_normal():
    assert code_postal("75001") is True


def test_code_postal_limite():
    assert code_postal("7500") is False  # trop court
    assert code_postal("750011") is False  # trop long
    assert code_postal("ABCDE") is False  # pas des chiffres
    assert code_postal("00123") is False  # commence par 00


def test_code_postal_erreur():
    with pytest.raises(ValueError):
        code_postal("")


def test_route_code_postal_normal():
    reponse = client.get("/validation/code_postal/75001")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_code_postal_erreur():
    reponse = client.get("/validation/code_postal/%20")
    assert reponse.status_code == 400
