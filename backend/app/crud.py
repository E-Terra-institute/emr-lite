from sqlalchemy.orm import Session
from app import models, schemas

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

