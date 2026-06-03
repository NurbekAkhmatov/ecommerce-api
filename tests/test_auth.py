# tests/test_auth.py
from app.auth import create_access_token

def test_register(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_register_duplicate(client, test_user):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123"
        }
    )
    assert response.status_code == 400

def test_login(client, test_user):
    response = client.post(
        "/auth/login",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client, test_user):
    response = client.post(
        "/auth/login",
        data={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401

def test_login_wrong_username(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "notexist",
            "password": "password123"
        }
    )
    assert response.status_code == 401

def test_protected_route_without_token(client):
    response = client.get("/cart/")
    assert response.status_code == 401

def test_protected_route_with_token(client, test_user):
    token = create_access_token(data={"sub": test_user.username})
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/cart/", headers=headers)
    assert response.status_code == 200