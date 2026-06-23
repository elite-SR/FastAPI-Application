from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code in [200, 503]

    data = response.json()

    if response.status_code == 503:
        data = data["detail"]["status"]

    assert "status" in data
    assert "database" in data
    assert "redis" in data