import pytest
from fastapi.testclient import TestClient
from app.core.config import settings
from app.main import app
from app.models.user_model import User
from app.services.user_service import UserService

url = "/api/v1/pokemon/"

test_username = settings.TEST_USERNAME
test_email = settings.TEST_EMAIL
test_password = settings.TEST_PASSWORD


class TestUserRoutes():
    # Classe que testa as rotas relacionadas aos dados do usuário
    @pytest.fixture()
    def client(self):
        return TestClient(app)

    def test_post_create_user(self, client):
        # Testa criação de usuário com dados válidos
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": test_password
            }
        )

        user = UserService.get_user_by_email("johndoe@gmail.com")
        if user:
            User.Meta.database.delete(f":app.models.user_model.User:{user.pk}")

        assert response.status_code == 200

    def test_post_create_user_invalid_email(self, client):
        # Testa criação de usuário com e-mail inválido
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
        # Testa criação de usuário com senha curta
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
        # Testa criação de usuário com nome de usuário curto
        response = client.post(
            "/api/v1/users/create/",
            json={
                "username": "john",
                "email": test_email,
                "password": test_password
            }
        )

        assert response.status_code == 422
