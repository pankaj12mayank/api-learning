from typing import Optional
from fastapi import APIRouter
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import *

router = APIRouter(tags=["inventory management"])

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    return create_product_services(product)

@router.get("/products", response_model=list[ProductResponse])
def get_products():
    return get_product_services()



@router.get("/products/{product_id}", response_model= Optional[ProductResponse])
def get_product_by_id(product_id: int):
        product = get_product_by_id_services(product_id)
        if product:
                return product
        return None



@router.put("/products/{product_id}", response_model=ProductResponse)
def updated_product(product_id: int, product: ProductCreate):
    updated = updated_product_services(product_id, product)
    
    if updated:
        return updated
    
    return None
    

@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    return delete_product_services(product_id)
