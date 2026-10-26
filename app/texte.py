from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/texte", tags=["texte"])


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


@router.get("/inverser")
def route_inverser(texte: str) -> dict[str, str]:
    """Inverse le texte reçu dans l'adresse (?texte=...)."""
    try:
        return {"resultat": inverser(texte)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur
