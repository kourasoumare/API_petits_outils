from fastapi import FastAPI
from app.routes import conversion

app = FastAPI(
    title="API de petits outils",
    version="0.1.0",
)

app.include_router(conversion.router)


@app.get("/sante")
def sante() -> dict[str, str]:
    """Indique que l'API est démarrée et répond."""
    return {"statut": "ok"}