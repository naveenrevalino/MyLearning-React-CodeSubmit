from pytest import mark

pytestmark = mark.dont_patch_engines


async def test_it(client, doctor_no, session):
    from toubib.sqla import Doctor

    doctor_id = doctor_no.id
    session.expunge(doctor_no)
    res = await client.delete(f"/v1/doctors/{doctor_id}")
    assert res.status_code == 204, (res.status_code, res.content)
    assert session.get(Doctor, doctor_id) is None


async def test_it_returns_404_on_not_found_doctor(client):
    res = await client.delete("/v1/doctors/1234567890")
    assert res.status_code == 404, (res.status_code, res.content)
