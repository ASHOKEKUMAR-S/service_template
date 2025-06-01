from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_apps_api():
    response = client.get("/apps")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
