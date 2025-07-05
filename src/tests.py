from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_home_page():
    path = "/"
    response = client.get(path)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
