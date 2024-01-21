import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.core.config import settings
from app.tests.helper import get_test_token

url = "/api/v1/pokemon/"

test_username = settings.TEST_USERNAME
test_email = settings.TEST_EMAIL
test_password = settings.TEST_PASSWORD


class TestAuthRoutes:
    # Classe que testa rotas relacionadas aos processos de autenticação
    @pytest.fixture()
    def client(self):
        return TestClient(app)

    @pytest.fixture
    def token(self, client):
        token = get_test_token(
            email=test_email,
            password=test_password,
            client=client
        ) 

        return token

    def test_post_login(self, client):
        # Testa login com credenciais corretas.
        response = client.post(
            "/api/v1/auth/login",
            data={
                "username": test_email,
                "password": test_password,
            },
            headers={"content-type": "application/x-www-form-urlencoded"}
        )

        assert response.status_code == 200

    def test_post_login_email_not_found(self, client):
        # Testa login com e-mail inexistente
        response = client.post(
            "/api/v1/auth/login",
            data={
                "username": "not_found@gmail.com",
                "password": test_password,
            },
            headers={"content-type": "application/x-www-form-urlencoded"}
        )

        assert response.status_code == 400
        assert response.json() == {"detail": "E-mail or password is incorrect"}

    def test_post_login_invalid_password(self, client):
        # Testa login com senha incorreta
        response = client.post(
            "/api/v1/auth/login",
            data={
                "username": test_email,
                "password": "123",
            },
            headers={"content-type": "application/x-www-form-urlencoded"}
        )

        assert response.status_code == 400
        assert response.json() == {"detail": "E-mail or password is incorrect"}

    def test_post_refresh_token(self, client, token):
        # Testa se o processo de geração de refresh_token está funcionando corretamente
        response = client.post(
            "/api/v1/auth/refresh/",
            json=f"{token.json()['access_token']}"
        )

        assert response.status_code == 200


