# app/routes/conversion.py
from fastapi import APIRouter, HTTPException
#HTTPE en attendant que erreurs.py existe 
router = APIRouter(prefix="/conversion", tags=["conversion"])


@router.get("/celsius_fahrenheit")
def celsius_fahrenheit(celsius: float):
    if celsius < -273.15:
        raise HTTPException(status_code=400, detail="Température inférieure au zéro absolu")
    return {"celsius": celsius, "fahrenheit": celsius * 9 / 5 + 32}

KM_EN_MILES = 0.621371


@router.get("/km_miles")
def km_miles(km: float):
    if km < 0:
        raise HTTPException(status_code=400, detail="Une distance ne peut pas être négative")
    return {"km": km, "miles": km * KM_EN_MILES}