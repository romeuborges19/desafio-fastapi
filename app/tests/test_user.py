import pytest
from fastapi.testclient import TestClient
from app.core.config import settings
from app.main import app
from app.schemas.user_schema import UserAuthentication

url = "/api/v1/pokemon/"

test_username = settings.TEST_USERNAME
test_email = settings.TEST_EMAIL
test_password = settings.TEST_PASSWORD


# Testa rotas que se comunicam com dados dos usuários
class TestUserRoutes():
    @pytest.fixture 
    def client(self):
        return TestClient(app)

    def test_post_create_user(self, client):
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": test_username,
                "email": test_email,
                "password": test_password
            }
        )

        assert response.status_code == 200

    def test_post_create_user_invalid_email(self, client):
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": test_username,
                "email": "invalid_email",
                "password": test_password
            }
        )

        assert response.status_code == 422

    def test_post_create_user_password_too_short(self, client):
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": test_username,
                "email": test_email,
                "password": "123"
            }
        )

        assert response.status_code == 422

    def test_post_create_user_username_too_short(self, client):
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": "john",
                "email": test_email,
                "password": test_password
            }
        )

        assert response.status_code == 422
