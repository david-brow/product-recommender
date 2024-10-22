from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_products
from ..schemas import Product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    products = get_products(db)
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products
