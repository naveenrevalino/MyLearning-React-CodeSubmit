from pytest import mark

pytestmark = mark.dont_patch_engines


async def test_it(client, patient_zero):
    res = await client.get(f"/v1/patients/{patient_zero.id}")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["id"] == patient_zero.id
    assert data["email"] == patient_zero.email
    assert data["first_name"] == patient_zero.first_name
    assert data["last_name"] == patient_zero.last_name
    assert data["date_of_birth"] == patient_zero.date_of_birth.isoformat()


async def test_it_returns_404_on_not_found(client):
    res = await client.get("/v1/patients/123456789")
    assert res.status_code == 404
