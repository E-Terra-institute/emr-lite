from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    full_name: str
    date_of_birth: date
    phone: str
    address: str | None = None

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    id: int

    class Config:
        orm_mode = True
