def test_add(session, faker):
    from toubib.sqla import Patient

    patient = Patient(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.unique.email(),
        date_of_birth=faker.date_of_birth(),
    )
    session.add(patient)
    session.flush()
    assert patient.id is not None
