# app/routes/conversion.py
from fastapi import APIRouter, HTTPException
#HTTPE en attendant que erreurs.py existe 
router = APIRouter(prefix="/conversion", tags=["conversion"])


@router.get("/celsius_fahrenheit")
def celsius_fahrenheit(celsius: float):
    if celsius < -273.15:
        raise HTTPException(status_code=400, detail="Température inférieure au zéro absolu")
    return {"celsius": celsius, "fahrenheit": celsius * 9 / 5 + 32}