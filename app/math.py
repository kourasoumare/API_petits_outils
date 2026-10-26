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


def est_premier(n: int) -> bool:
    """Renvoie True si n est un nombre premier et False sinon, en levant ValueError si n n'est pas un entier positif ou nul."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n doit être un entier positif ou nul")
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


@router.get("/est_premier/{n}")
def route_est_premier(n: int):
    try:
        return {"resultat": est_premier(n)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
