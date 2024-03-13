from fastapi.testclient import TestClient
from ...toubib.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_sqla import Base


DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    poolclass=staticmethod,
    )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

def override_get_db(): 
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_sqla_getPatient():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "OK"

def test_getPatients():
    response = client.get(
        "/items/", json={"email": "EmailStr",
    "first_name": "str",
    "last_name": "str",
    "date_of_birth": "date"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "EmailStr"
    assert data["first_name"] == "str"
    assert data["last_name"] == "str"
    assert data["date_of_birth"] == "date"

def setup():
    Base.metadata.create_all(bind=engine)

def teardown():
    Base.metadata.drop_all(bind=engine)

