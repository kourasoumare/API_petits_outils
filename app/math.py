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


def est_premier(n):
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


def pgcd(a, b):
    if (
        not isinstance(a, int)
        or not isinstance(b, int)
        or a <= 0
        or b <= 0
    ):
        raise ValueError("a et b doivent être des entiers strictement positifs")
    resultat = 1 
    for  d in range(1 , min(a,b)+1):
        if  a % d == 0 and b % d == 0:
            resultat = d
    return resultat 

@router.get("/pgcd/{a}/{b}") 
def route_pgcd(a: int,b: int):
    try:
        return {"resultat": pgcd(a,b)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
           
        