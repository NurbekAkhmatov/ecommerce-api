from app.auth import create_access_token

def test_create_category(client, test_user):
    token = create_access_token(data={"sub": test_user.username})
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post(
        "/categories/",
        json={
            "name": "Yangi Kategoriya",
            "slug": "yangi-kategoriya",
            "description": "Test uchun kategoriya"
        },
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Yangi Kategoriya"
    assert data["slug"] == "yangi-kategoriya"

def test_create_category_without_auth(client):
    response = client.post(
        "/categories/",
        json={
            "name": "Authsiz Kategoriya",
            "slug": "authsiz",
            "description": "Bu ishlamasligi kerak"
        }
    )
    assert response.status_code == 401

def test_get_all_categories(client, test_category):
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

def test_get_category_by_id(client, test_category):
    # Avval kategoriya borligini tekshirish
    get_all = client.get("/categories/")
    categories = get_all.json()
    assert len(categories) > 0
    
    # Birinchi kategoriyani olish
    category_id = categories[0]["id"]
    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200

def test_get_category_not_found(client):
    response = client.get("/categories/99999")
    assert response.status_code == 404

def test_update_category(client, test_user):
    # Avval kategoriya yaratamiz
    token = create_access_token(data={"sub": test_user.username})
    headers = {"Authorization": f"Bearer {token}"}
    
    create_response = client.post(
        "/categories/",
        json={
            "name": "Update Test Kategoriya",
            "slug": "update-test",
            "description": "Yangilash uchun"
        },
        headers=headers
    )
    category_id = create_response.json()["id"]
    
    # Yangilash
    update_response = client.put(
        f"/categories/{category_id}",
        json={"name": "Yangilangan Nomi"},
        headers=headers
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Yangilangan Nomi"

def test_delete_category(client, test_user):
    # Avval kategoriya yaratamiz
    token = create_access_token(data={"sub": test_user.username})
    headers = {"Authorization": f"Bearer {token}"}
    
    create_response = client.post(
        "/categories/",
        json={
            "name": "Delete Test Kategoriya",
            "slug": "delete-test",
            "description": "O'chirish uchun"
        },
        headers=headers
    )
    category_id = create_response.json()["id"]
    
    # O'chirish
    delete_response = client.delete(f"/categories/{category_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Kategoriya muvaffaqiyatli o'chirildi"
    
    # O'chirilganligini tekshirish
    get_response = client.get(f"/categories/{category_id}")
    assert get_response.status_code == 404