from fastapi_sqla import Base


class Doctor(Base):
    __tablename__ = "doctor"


class Patient(Base):
    __tablename__ = "patient"
