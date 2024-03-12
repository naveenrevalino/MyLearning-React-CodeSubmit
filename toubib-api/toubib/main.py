from datetime import date
from http import HTTPStatus
from importlib.metadata import version

import fastapi_sqla
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqla import Item, Session, Page, Paginate
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel, ConfigDict, EmailStr
from structlog import get_logger

from toubib.sqla import Doctor, Patient

log = get_logger()

app = FastAPI(title="toubib", version=version("toubib"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_sqla.setup(app)


@app.get("/health")
def health():
    "Return OK if app is reachable"
    return "OK"


class DoctorIn(BaseModel):
    first_name: str
    last_name: str
    hiring_date: date
    specialization: str


class DoctorModel(DoctorIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


@app.post("/v1/doctors", response_model=Item[DoctorModel], status_code=201)
def create_doctor(*, body: DoctorIn, session: Session):
    doctor = Doctor(**body.model_dump())
    session.add(doctor)
    session.flush()
    return {"data": doctor}


@app.get("/v1/doctors/{doctor_id}", response_model=Item[DoctorModel])
def get_doctor(*, doctor_id: int, session: Session):
    doctor = session.get(Doctor, doctor_id)
    if doctor is None:
        raise HTTPException(HTTPStatus.NOT_FOUND)
    return {"data": doctor}


@app.delete("/v1/doctors/{doctor_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_doctor(*, doctor_id: int, session: Session):
    stmt = delete(Doctor).where(Doctor.id == doctor_id)
    res = session.execute(stmt)
    if not res.rowcount:
        raise HTTPException(HTTPStatus.NOT_FOUND)


class PatientIn(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    date_of_birth: date


class PatientModel(PatientIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


@app.get("/v1/patients", response_model=Page[PatientModel])
def list_patients(paginate: Paginate):
    return paginate(select(Patient))


@app.post("/v1/patients", response_model=Item[PatientModel], status_code=201)
def create_patient(*, body: PatientIn, session: Session):
    patient = Patient(**body.model_dump())
    session.add(patient)
    try:
        session.flush()
    except IntegrityError as error:
        if "UNIQUE constraint failed" in str(error):
            raise HTTPException(HTTPStatus.CONFLICT)
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR)  # pragma: no cover
    return {"data": patient}


@app.get("/v1/patients/{patient_id}", response_model=Item[PatientModel])
def get_patient(*, patient_id: int, session: Session):
    patient = session.get(Patient, patient_id)
    if patient is None:
        raise HTTPException(HTTPStatus.NOT_FOUND)
    return {"data": patient}


# FIXME: 🥸 Add the endpoint to delete a patient
# Delete API for patient
@app.delete("/v1/patients/{patient_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_patient(*, patient_id: int, session: Session):
    stmt = delete(Patient).where(Patient.id == patient_id)
    res = session.execute(stmt)
    if not res.rowcount:
        raise HTTPException(HTTPStatus.NOT_FOUND)
