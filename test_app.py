import pytest

from app import app


@pytest.fixture
def client(monkeypatch):
    client = app.test_client()
    monkeypatch.setattr("app.service_states", {"ssh": "running", "NetworkManager": "stopped"})
    return client

def test_health(client):
#    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "ok"

def test_missing_route(client):
#    client = app.test_client() 
    response = client.get("/missing")

    assert response.status_code == 404

def test_get_services(client):
    response = client.get("/services")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'NetworkManager': 'stopped', 'ssh': 'running'}

def test_get_ssh_status(client):
    responce = client.get("/services/ssh")
    assert responce.status_code == 200
    data = responce.get_data(as_text=True)
    assert data == "running"
    # ИЛИ одной строкой без data
    assert responce.get_data(as_text=True) == "running"

def test_unknown_service(client):
    response = client.get("/services/cron")
    assert response.status_code == 404
    data = response.get_data(as_text=True)
    assert data == "Service not found"

@pytest.mark.parametrize("status", ["stopped", "running"])
def test_create_service(client, status):
    responce = client.post("/services", json={"name": "cron", "status": status})
    assert responce.status_code == 201

    check_code = client.get("/services/cron")
    get_status = check_code.get_data(as_text=True)
    assert check_code.status_code == 200
    assert get_status == status

def test_create_service_without_status(client):
    response = client.post("/services", json={"name": "cron"})
    assert response.status_code == 400
    response = client.get("/services/cron")
    assert response.status_code == 404

def test_create_service_without_name(client):
    responce = client.post("/services", json={"status": "running"})
    assert responce.status_code == 400

def test_create_existing_service(client):
    responce = client.post("/services", json={"name": "ssh", "status": "stopped"})
    assert responce.status_code == 409
    responce = client.get("/services/ssh")
    data = responce.get_data(as_text=True)
    assert data == "running"

def test_update_service_status(client):
    responce = client.patch("/services/ssh", json={"status": "stopped"})
    assert responce.status_code == 200
    responce = client.get("/services/ssh")
    data = responce.get_data(as_text=True)
    assert data == "stopped"

def test_update_unknown_service(client):
    responce = client.patch("/services/cron", json={"status": "stopped"})
    assert responce.status_code == 404
    responce = client.get("/services/cron")
    assert responce.status_code == 404

def test_update_service_without_status(client):
    responce = client.patch("/services/ssh", json={})
    assert responce.status_code == 400
    responce = client.get("/services/ssh")
    data = responce.get_data(as_text=True)
    assert data == "running"

def test_delete_service(client):
    responce = client.delete("/services/ssh")
    assert responce.status_code == 204
    responce = client.get("/services/ssh")
    assert responce.status_code == 404
    #data = responce.get_data(as_text=True)

def test_delete_unknown_service(client):
    responce = client.delete("/services/cron")
    assert responce.status_code == 404

def test_create_service_with_empty_status(client):
    response = client.post("/services", json={"name": "cron", "status": ""})
    assert response.status_code == 400
    response = client.get("/services/cron")
    assert response.status_code == 404

def test_exersice_1(client):
    responce = client.patch("/services/ssh", json={"status": ""})
    assert responce.status_code == 400
    responce = client.get("/services/ssh")
    data = responce.get_data(as_text=True)
    assert data == "running"

def test_create_service_with_empty_name(client):
    responce = client.post("/services", json={"name": "", "status": "running"})
    assert responce.status_code == 400