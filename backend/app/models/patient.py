from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String)

