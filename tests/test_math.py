import pytest

from app.math import factorielle


def test_factorielle_normal():
    assert factorielle(5) == 120


def test_factorielle_limite():
    assert factorielle(0) == 1


def test_factorielle_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)