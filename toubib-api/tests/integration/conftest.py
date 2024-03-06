from pytest import fixture


@fixture
def patient_zero(faker, session):
    from toubib.sqla import Patient

    patient = Patient(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.unique.email(),
        date_of_birth=faker.date_of_birth(),
    )
    session.add(patient)
    session.commit()
    return patient


@fixture
def doctor_no(faker, session):
    from toubib.sqla import Doctor

    doctor = Doctor(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        hiring_date=faker.date_object(),
        specialization=faker.bs(),
    )
    session.add(doctor)
    session.commit()
    return doctor
