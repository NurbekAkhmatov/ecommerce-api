from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class CartBase(BaseModel):
    product_id: int
    quantity: int = 1

class CartCreate(CartBase):
    pass

class CartUpdate(BaseModel):
    quantity: int

class CartResponse(CartBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None  # <-- Optional qiling!

    model_config = ConfigDict(from_attributes=True)