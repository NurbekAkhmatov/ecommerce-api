from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    # Ma'lumotlar bazasi
    DATABASE_URL: str = "postgresql://postgres:1234567@localhost:5432/ecommerce_db"
    
    # Xavfsizlik
    SECRET_KEY: str = "mening-maxfiy-kalitim-123456789"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Stripe (to'lov)
    STRIPE_SECRET_KEY: str = "sk_test_placeholder"
    
    # Email
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    EMAIL_USER: str = "placeholder@gmail.com"
    EMAIL_PASSWORD: str = "placeholder"

settings = Settings()