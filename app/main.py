from fastapi import FastAPI

app = FastAPI(
    title="API de petits outils",
    version="0.1.0",
)


@app.get("/sante")
def sante() -> dict[str, str]:
    """Indique que l'API est démarrée et répond."""
    return {"statut": "ok"}