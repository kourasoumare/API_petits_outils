from fastapi import APIRouter, HTTPException

router = APIRouter()

def factorielle(n):
    if not isinstance(n,int) or n < 0:
         raise ValueError("n doit être un entier positif ou nul")
    resultat = 1
    for i in range(2,n+1):
        resultat = resultat * i
    return resultat


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"resultat": factorielle(n)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))

    