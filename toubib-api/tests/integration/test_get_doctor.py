from pytest import mark

pytestmark = mark.dont_patch_engines


async def test_it(client, doctor_no):
    res = await client.get(f"/v1/doctors/{doctor_no.id}")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["id"] == doctor_no.id
    assert data["first_name"] == doctor_no.first_name
    assert data["last_name"] == doctor_no.last_name
    assert data["hiring_date"] == doctor_no.hiring_date.isoformat()
    assert data["specialization"] == doctor_no.specialization


async def test_it_returns_404_on_not_found(client):
    res = await client.get("/v1/doctors/123456789")
    assert res.status_code == 404
