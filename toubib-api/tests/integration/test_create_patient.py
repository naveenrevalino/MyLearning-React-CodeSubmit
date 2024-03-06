from pytest import mark

pytestmark = mark.dont_patch_engines


async def test_it(client, faker):
    body = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.unique.email(),
        "date_of_birth": faker.date_of_birth().isoformat(),
    }
    res = await client.post("/v1/patients", json=body)
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["id"] is not None
    assert data["first_name"] == body["first_name"]
    assert data["last_name"] == body["last_name"]
    assert data["email"] == body["email"]
    assert data["date_of_birth"] == body["date_of_birth"]


async def test_it_returns_409_on_duplicate_email(client, patient_zero, faker):
    body = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": patient_zero.email,
        "date_of_birth": faker.date_of_birth().isoformat(),
    }
    res = await client.post("/v1/patients", json=body)

    assert res.status_code == 409, (res.status_code, res.content)
