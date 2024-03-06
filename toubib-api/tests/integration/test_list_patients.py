async def test_it(client):
    res = await client.get("/v1/patients")
    assert res.status_code == 200
    json_res = res.json()

    data = json_res["data"]
    meta = json_res["meta"]

    assert len(data) == 10
    meta_keys = meta.keys()
    assert "total_items" in meta_keys
    assert "page_number" in meta_keys
    assert "offset" in meta_keys
    assert "total_pages" in meta_keys


async def test_it_returns_404_on_not_found_doctor(client):
    res = await client.get("/v1/doctors/123456789")
    assert res.status_code == 404
