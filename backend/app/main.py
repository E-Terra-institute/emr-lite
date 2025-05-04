from fastapi import FastAPI
from app.api.routes import patient
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="EMR-lite")

Base.metadata.create_all(bind=engine)

app.include_router(patient.router, prefix="/patients", tags=["Patients"])
