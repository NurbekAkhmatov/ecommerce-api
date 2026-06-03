import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import Base, get_db
from app.models import User, Category, Product
from app.auth import get_password_hash, create_access_token

# SQLite in-memory database (StaticPool bilan)
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def test_user(client):
    db = TestingSessionLocal()
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=get_password_hash("testpass"),
        is_active=True,
        is_admin=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user


@pytest.fixture(scope="function")
def test_user_token(test_user):
    return create_access_token(data={"sub": test_user.username})


@pytest.fixture(scope="function")
def test_category(client):
    db = TestingSessionLocal()
    category = Category(
        name="Test Category",
        slug="test-category",
        description="Test description"
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    db.close()
    return category


@pytest.fixture(scope="function")
def test_product(client, test_category):
    db = TestingSessionLocal()
    product = Product(
        name="Test Product",
        slug="test-product",
        description="Test description",
        price=99.99,
        stock=10,
        category_id=test_category.id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return product