import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.math import est_premier, factorielle, pgcd

client = TestClient(app)




def test_factorielle_normal():
    assert factorielle(5) == 120


def test_factorielle_limite():
    assert factorielle(0) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)


def test_route_factorielle_normal():
    reponse = client.get("/factorielle/5")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": 120}


def test_route_factorielle_erreur():
    reponse = client.get("/factorielle/-1")
    assert reponse.status_code == 400

def test_est_premier_normal():
    assert est_premier(7) is True
    assert est_premier(9) is False


def test_est_premier_limite():
    assert est_premier(0) is False
    assert est_premier(1) is False
    assert est_premier(2) is True


def test_est_premier_erreur():
    with pytest.raises(ValueError):
        est_premier(-1)
   
    
def test_route_est_premier_normal():
    reponse = client.get("/est_premier/7")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": True}


def test_route_est_premier_erreur():
    reponse = client.get("/est_premier/-1")
    assert reponse.status_code == 400


def test_pgcd_normal():
    assert pgcd(8, 12) == 4
    


def test_pgcd_limite():
    assert pgcd(1, 7) == 1
    


def test_pgcd_erreur():
    with pytest.raises(ValueError):
        pgcd(0, 5)


def test_route_pgcd_normal():
    reponse = client.get("/pgcd/6/9")
    assert reponse.status_code == 200
    assert reponse.json() == {"resultat": 3}


def test_route_pgcd_erreur():
    reponse = client.get("/pgcd/0/5")
    assert reponse.status_code == 400   