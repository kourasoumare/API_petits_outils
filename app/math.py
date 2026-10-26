from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/math", tags=["math"])


def factorielle(n: int) -> int:
    """Renvoie n! (produit des entiers de 1 à n). Lève ValueError si n < 0."""
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")
    resultat = 1
    for i in range(2, n + 1):
        resultat = resultat * i
    return resultat


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"resultat": factorielle(n)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
