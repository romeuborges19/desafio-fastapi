import pytest
from fastapi.testclient import TestClient
from app.core.config import settings
from app.main import app
from app.tests.helper import get_test_token

# client = TestClient(app)
url = "/api/v1/pokemon/"

test_email = settings.TEST_EMAIL
test_password = settings.TEST_PASSWORD


# Testa rota que obtém dados de pokémons
class TestPokemonRoutes():
    @pytest.fixture 
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

    def test_read_pokemon(self, client, token):
        response = client.get(
            f"{url}charizard",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_pokemon_not_found(self, client, token):
        response = client.get(
            f"{url}johndoe",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )  

        assert response.status_code == 404

    def test_read_pokemon_encounter(self, client, token):
        response = client.get(
            f"{url}ditto/encounters",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        ) 

        assert response.status_code == 200

    def test_read_pokemon_encounter_no_content(self, client, token):
        response = client.get(
            f"{url}charizard/encounters",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 204

