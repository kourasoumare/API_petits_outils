"""Module validation : email_valide, mdp_robuste, code_postal."""

import re

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/validation", tags=["validation"])

EMAIL_VIDE = "L'email ne peut pas être vide."

_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)


def email_valide(email: str) -> bool:
    """Vrai si l'email a un format valide (ex : nom@domaine.fr)."""
    if not email or not email.strip():
        raise ValueError(EMAIL_VIDE)
    email = email.strip()
    if ".." in email:
        return False
    return bool(_EMAIL_RE.match(email))


@router.get("/email/{valeur}")
def route_email_valide(valeur: str) -> dict[str, bool]:
    try:
        return {"resultat": email_valide(valeur)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
