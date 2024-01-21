import pytest
from fastapi.testclient import TestClient
from app.core.config import settings
from app.main import app
from app.tests.helper import get_test_token

url = "/api/v1/pokemon/"

test_email = settings.TEST_EMAIL
test_password = settings.TEST_PASSWORD


class TestPokemonRoutes():
    # Classe que testa as rotas relacionadas ao consumo da PokéAPI e 
    # seus possíveis retornos
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

    def test_read_pokemon(self, client, token):
        # Testa se a API retorna dados para a pesquisa de um pokémon existente
        response = client.get(
            f"{url}charizard",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_pokemon_not_found(self, client, token):
        # Testa se a API retorna dados para a pesquisa de um pokémon inexistente
        response = client.get(
            f"{url}johndoe",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )  

        assert response.status_code == 404

    def test_read_pokemon_encounter(self, client, token):
        # Testa se a API retorna dados para a pesquisa sobre informações de encontro de um
        # Pokémon existente
        response = client.get(
            f"{url}ditto/encounters",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        ) 

        assert response.status_code == 200

    def test_read_pokemon_encounter_not_found(self, client, token):
        # Testa se a API retorna dados para a pesquisa sobre informações de encontro de um
        # Pokémon inexistente
        response = client.get(
            f"{url}johndoe/encounters",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        ) 

        assert response.status_code == 404

    def test_read_pokemon_encounter_no_content(self, client, token):
        # Testa se a API identifica a ausência de conteúdo de um retorno da PokéAPI
        response = client.get(
            f"{url}charizard/encounters",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 204

    def test_read_habitat(self, client, token):
        response = client.get(
            f"{url}habitat/cave",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_habitat_not_found(self, client, token):
        response = client.get(
            f"{url}habitat/123",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 404

    def test_read_color(self, client, token):
        response = client.get(
            f"{url}color/black",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_color_not_found(self, client, token):
        response = client.get(
            f"{url}color/123",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 404

    def test_read_ability(self, client, token):
        response = client.get(
            f"{url}ability/stench",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_ability_not_found(self, client, token):
        response = client.get(
            f"{url}ability/notfound",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 404

    def test_read_type(self, client, token):
        response = client.get(
            f"{url}type/ice",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_type_not_found(self, client, token):
        response = client.get(
            f"{url}type/notfound",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 404

    def test_read_species(self, client, token):
        response = client.get(
            f"{url}species/wormadam",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 200

    def test_read_species_not_found(self, client, token):
        response = client.get(
            f"{url}species/nottfound",
            headers={"Authorization": f"Bearer {token.json()['access_token']}"}
        )

        assert response.status_code == 404
