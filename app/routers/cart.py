from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Cart, Product, User
from app.schemas import CartCreate, CartUpdate, CartResponse
from app.auth import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(
    cart_item: CartCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Savatga mahsulot qo'shish"""
    # Mahsulot mavjudligini tekshirish
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahsulot topilmadi"
        )
    
    # Mahsulot allaqachon savatdami?
    existing = db.query(Cart).filter(
        Cart.user_id == current_user.id,
        Cart.product_id == cart_item.product_id
    ).first()
    
    if existing:
        # Bor bo'lsa, miqdorini oshirish
        existing.quantity += cart_item.quantity
        db.commit()
        db.refresh(existing)
        return existing
    
    # Yangi mahsulot qo'shish
    new_cart_item = Cart(
        user_id=current_user.id,
        product_id=cart_item.product_id,
        quantity=cart_item.quantity
    )
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return new_cart_item

@router.get("/", response_model=List[CartResponse])
def get_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Foydalanuvchining savatini ko'rish"""
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    return cart_items

@router.put("/{cart_item_id}", response_model=CartResponse)
def update_cart_item(
    cart_item_id: int,
    cart_update: CartUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Savatdagi mahsulot miqdorini yangilash"""
    cart_item = db.query(Cart).filter(
        Cart.id == cart_item_id,
        Cart.user_id == current_user.id
    ).first()
    
    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Savatdagi mahsulot topilmadi"
        )
    
    cart_item.quantity = cart_update.quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.delete("/{cart_item_id}")
def remove_from_cart(
    cart_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Savatdan mahsulot o'chirish"""
    cart_item = db.query(Cart).filter(
        Cart.id == cart_item_id,
        Cart.user_id == current_user.id
    ).first()
    
    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Savatdagi mahsulot topilmadi"
        )
    
    db.delete(cart_item)
    db.commit()
    return {"message": "Mahsulot savatdan o'chirildi"}

@router.delete("/")
def clear_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Butun savatni tozalash"""
    db.query(Cart).filter(Cart.user_id == current_user.id).delete()
    db.commit()
    return {"message": "Savat tozalandi"}