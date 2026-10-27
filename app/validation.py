"""Module validation : email_valide, mdp_robuste, code_postal."""

import re

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/validation", tags=["validation"])

EMAIL_VIDE = "L'email ne peut pas être vide."
MDP_VIDE = "Le mot de passe ne peut pas être vide."
CODE_POSTAL_VIDE = "Le code postal ne peut pas être vide."

_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)
_CODE_POSTAL_RE = re.compile(r"^\d{5}$")


def email_valide(email: str) -> bool:
    """Vrai si l'email a un format valide (ex : nom@domaine.fr)."""
    if not email or not email.strip():
        raise ValueError(EMAIL_VIDE)
    email = email.strip()
    if ".." in email:
        return False
    return bool(_EMAIL_RE.match(email))


def mdp_robuste(mdp: str) -> bool:
    """Vrai si le mot de passe a au moins 8 caractères, une majuscule,
    une minuscule, un chiffre et un caractère spécial."""
    if not mdp or not mdp.strip():
        raise ValueError(MDP_VIDE)
    return (
        len(mdp) >= 8
        and any(c.isupper() for c in mdp)
        and any(c.islower() for c in mdp)
        and any(c.isdigit() for c in mdp)
        and any(not c.isalnum() for c in mdp)
    )


def code_postal(code: str) -> bool:
    """Vrai si le code postal français est valide : 5 chiffres, sans commencer par 00."""
    if not code or not code.strip():
        raise ValueError(CODE_POSTAL_VIDE)
    code = code.strip()
    if not _CODE_POSTAL_RE.match(code):
        return False
    return not code.startswith("00")


@router.get("/email/{valeur}")
def route_email_valide(valeur: str) -> dict[str, bool]:
    try:
        return {"resultat": email_valide(valeur)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))


@router.get("/mdp/{valeur}")
def route_mdp_robuste(valeur: str) -> dict[str, bool]:
    try:
        return {"resultat": mdp_robuste(valeur)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))


@router.get("/code-postal/{valeur}")
def route_code_postal(valeur: str) -> dict[str, bool]:
    try:
        return {"resultat": code_postal(valeur)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur))
