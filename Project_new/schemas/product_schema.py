from pydantic import BaseModel

class ProductCreate(BaseModel):
    id: int
    pname: str
    price: int
    qty: int
    meg: str


class ProductResponse(BaseModel):
    id: int
    pname: str
    price: int
    qty: int
    meg: str

    class Config:
        from_attributes = True   # ✅ VERY IMPORTANT