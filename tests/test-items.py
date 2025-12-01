from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "API CRUD básica con FastAPI"}


def test_create_item():
    resp = client.post("/items", json={"name": "Item 1", "description": "desc"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == 1
    assert data["name"] == "Item 1"


def test_list_items():
    # Ya debería existir al menos el id=1 del test anterior
    resp = client.get("/items")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_item():
    resp = client.get("/items/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1


def test_update_item():
    resp = client.put("/items/1", json={"name": "Item 1 editado", "description": "nueva desc"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Item 1 editado"


def test_delete_item():
    resp = client.delete("/items/1")
    assert resp.status_code == 204

    # verificar que ya no exista
    resp2 = client.get("/items/1")
    assert resp2.status_code == 404
