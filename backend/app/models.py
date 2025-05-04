from sqlalchemy import Column, Integer, String, Date
from app.db import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(Date)
    phone = Column(String)
    address = Column(String, nullable=True)
