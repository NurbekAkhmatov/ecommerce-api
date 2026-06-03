from app.auth import create_access_token

def test_create_product(client, test_user, test_category):
    token = create_access_token(data={"sub": test_user.username})
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post(
        "/products/",
        json={
            "name": "Test Mahsulot",
            "slug": "test-mahsulot",
            "description": "Test uchun mahsulot",
            "price": 49.99,
            "stock": 100,
            "category_id": test_category.id
        },
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Mahsulot"
    assert data["price"] == 49.99

def test_get_all_products(client, test_product):
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

def test_get_product_by_id(client, test_product):
    response = client.get(f"/products/{test_product.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_product.id
    assert data["name"] == "Test Product"

def test_filter_products_by_price(client, test_product):
    response = client.get("/products/?min_price=50&max_price=150")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

def test_search_products(client, test_product):
    response = client.get("/products/?search=Test")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert "Test" in data[0]["name"]