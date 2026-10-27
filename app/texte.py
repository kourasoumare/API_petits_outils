from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/texte", tags=["texte"])


# Fonctions


# inverser une chaîne de caractères
def inverser(mot: str) -> str:
    """Renvoie le texte lu de droite à gauche. Lève une erreur si le texte est invalide."""
    if not isinstance(mot, str):
        raise TypeError("Le mot doit être une chaîne de caractères.")
    elif mot == "":
        raise ValueError("Le mot ne peut pas être vide.")
    elif mot.strip() == "":
        raise ValueError("Le mot ne peut pas être composé uniquement d'espaces.")
    else:
        return mot[::-1]


# palindrome
def est_palindrome(mot: str) -> bool:
    """Indique si le texte se lit pareil dans les deux sens, sans tenir compte des majuscules ni des espaces."""
    if not isinstance(mot, str):
        raise TypeError("Le mot doit être une chaîne de caractères.")
    texte_nettoye = mot.lower().replace(" ", "")
    return texte_nettoye == inverser(texte_nettoye)


# Routes


@router.get("/inverser")
def route_inverser(texte: str) -> dict[str, str]:
    """Inverse le texte reçu dans l'adresse (?texte=...)."""
    try:
        return {"resultat": inverser(texte)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur


@router.get("/est_palindrome")
def route_est_palindrome(texte: str) -> dict[str, bool]:
    """Indique si le texte reçu dans l'adresse (?texte=...) est un palindrome."""
    try:
        return {"resultat": est_palindrome(texte)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur
