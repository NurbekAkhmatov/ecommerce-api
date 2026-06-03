from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderBase(BaseModel):
    shipping_address: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None

class OrderResponse(OrderBase):
    id: int
    total_amount: float
    status: OrderStatus
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None  # <-- Optional qiling!
    items: List[OrderItemSchema] = []

    model_config = ConfigDict(from_attributes=True)
    