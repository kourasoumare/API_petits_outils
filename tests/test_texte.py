import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.texte import inverser

client = TestClient(app)


# --- Tests de la fonction inverser ---


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


# --- Tests de la route /texte/inverser ---


def test_route_inverser_renvoie_le_resultat():
    reponse = client.get("/texte/inverser", params={"texte": "bonjour"})
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": "ruojnob"}


def test_route_inverser_texte_vide_renvoie_400():
    reponse = client.get("/texte/inverser", params={"texte": ""})
    assert reponse.status_code == 400
