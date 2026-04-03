from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category: str

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category: str

    class Config:
        from_attributes = True