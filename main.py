from os import getenv

from fastapi import FastAPI

app = FastAPI(title="LAB9 - API FastAPI")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "ambiente": getenv("APP_ENV", "local")}
