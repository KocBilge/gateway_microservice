from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Gateway is running!"}

def test_get_user(mocker):
    mock_service = mocker.patch("services.user_service.UserService.get_user")
    mock_service.return_value = {"id": 1, "name": "John Doe"}

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}
