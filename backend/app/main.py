from fastapi import FastAPI
from app.api import patients
from app.db import create_db

app = FastAPI(title="EMR-lite API")

app.include_router(patients.router, prefix="/patients")

@app.on_event("startup")
def startup():
    create_db()

