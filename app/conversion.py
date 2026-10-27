from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/conversion", tags=["conversion"])

ZERO_ABSOLU = -273.15
KM_EN_MILES = 0.621371
TAUX_EURO = {"USD": 1.08, "GBP": 0.85, "JPY": 162.0, "CHF": 0.94}


# Fonctions


def celsius_fahrenheit(celsius: float) -> float:
    """Convertit des degrés Celsius en Fahrenheit. Lève une erreur sous le zéro absolu."""
    if celsius < ZERO_ABSOLU:
        raise ValueError("La température ne peut pas être inférieure au zéro absolu.")
    return celsius * 9 / 5 + 32


def km_miles(km: float) -> float:
    """Convertit des kilomètres en miles. Lève une erreur si la distance est négative."""
    if km < 0:
        raise ValueError("La distance ne peut pas être négative.")
    return km * KM_EN_MILES


def euros_devise(montant: float, devise: str) -> float:
    """Convertit un montant en euros vers une devise (taux fixes). Lève une erreur si l'entrée est invalide."""
    devise = devise.upper()
    if devise not in TAUX_EURO:
        raise ValueError(f"Devise inconnue : {devise}.")
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif.")
    return round(montant * TAUX_EURO[devise], 2)



# Routes


@router.get("/celsius_fahrenheit")
def route_celsius_fahrenheit(celsius: float) -> dict[str, float]:
    """Convertit la température reçue dans l'adresse (?celsius=...)."""
    try:
        return {"resultat": celsius_fahrenheit(celsius)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur


@router.get("/km_miles")
def route_km_miles(km: float) -> dict[str, float]:
    """Convertit la distance reçue dans l'adresse (?km=...)."""
    try:
        return {"resultat": km_miles(km)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur


@router.get("/euros_devise")
def route_euros_devise(montant: float, devise: str) -> dict[str, float]:
    """Convertit le montant reçu dans l'adresse (?montant=...&devise=...)."""
    try:
        return {"resultat": euros_devise(montant, devise)}
    except ValueError as erreur:
        raise HTTPException(status_code=400, detail=str(erreur)) from erreur