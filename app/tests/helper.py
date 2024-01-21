from fastapi.testclient import TestClient


def get_test_token(email:str, password:str, client: TestClient):
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": email,
            "password": password,
        },
        headers={"content-type": "application/x-www-form-urlencoded"}
    )

    return response
