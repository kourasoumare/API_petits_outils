from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sante_renvoie_code_200():
    reponse = client.get("/sante")
    assert reponse.status_code == 200


def test_sante_renvoie_statut_ok():
    reponse = client.get("/sante")
    assert reponse.json() == {"statut": "ok"}