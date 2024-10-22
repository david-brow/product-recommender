from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    name: str
    category: str | None
    price: float

    class Config:
        orm_mode = True
