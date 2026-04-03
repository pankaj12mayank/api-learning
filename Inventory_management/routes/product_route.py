from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import *

router = APIRouter()

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_service(product, db)


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_products_service(db)



@router.get("/products/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    return get_product_service(id, db)



@router.put("/products/{product_id}", response_model=ProductResponse)
def updated_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return update_product_service(product_id, product, db)
    

@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product_service(product_id, db)
