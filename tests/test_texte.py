import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.texte import est_palindrome, inverser

client = TestClient(app)


#  Tests de la fonction inverser ---


def test_inverser_cas_normal():
    assert inverser("bonjour") == "ruojnob"


def test_inverser_cas_limite_un_seul_caractere():
    assert inverser("a") == "a"


def test_inverser_cas_erreur_texte_vide():
    with pytest.raises(ValueError):
        inverser("")


def test_inverser_cas_erreur_uniquement_des_espaces():
    with pytest.raises(ValueError):
        inverser("   ")


def test_inverser_cas_erreur_pas_une_chaine():
    with pytest.raises(TypeError):
        inverser(None)


#  Tests de la route /texte/inverser


def test_route_inverser_renvoie_le_resultat():
    reponse = client.get("/texte/inverser", params={"texte": "bonjour"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": "ruojnob"}


def test_route_inverser_texte_vide_renvoie_400():
    reponse = client.get("/texte/inverser", params={"texte": ""})
    assert reponse.status_code == 400


#  Tests de la fonction est_palindrome


def test_est_palindrome_cas_normal_vrai():
    assert est_palindrome("kayak") is True


def test_est_palindrome_cas_normal_faux():
    assert est_palindrome("bonjour") is False


def test_est_palindrome_cas_limite_majuscules():
    assert est_palindrome("Kayak") is True


def test_est_palindrome_cas_limite_phrase_avec_espaces():
    assert est_palindrome("esope reste ici et se repose") is True


def test_est_palindrome_cas_limite_un_seul_caractere():
    assert est_palindrome("a") is True


def test_est_palindrome_cas_erreur_texte_vide():
    with pytest.raises(ValueError):
        est_palindrome("")


def test_est_palindrome_cas_erreur_uniquement_des_espaces():
    with pytest.raises(ValueError):
        est_palindrome("   ")


def test_est_palindrome_cas_erreur_pas_une_chaine():
    with pytest.raises(TypeError):
        est_palindrome(None)


#  Tests de la route /texte/est_palindrome


def test_route_est_palindrome_renvoie_vrai():
    reponse = client.get("/texte/est_palindrome", params={"texte": "kayak"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_est_palindrome_renvoie_faux():
    reponse = client.get("/texte/est_palindrome", params={"texte": "bonjour"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": False}


def test_route_est_palindrome_texte_vide_renvoie_400():
    reponse = client.get("/texte/est_palindrome", params={"texte": ""})
    assert reponse.status_code == 400
