from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.patient import PatientCreate, PatientOut
from app.crud.patient import get_all, create

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PatientOut])
def list_patients(db: Session = Depends(get_db)):
    return get_all(db)

@router.post("/", response_model=PatientOut)
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create(db, patient)
