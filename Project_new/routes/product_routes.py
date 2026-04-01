from fastapi import APIRouter
from schemas.product_schema import ProductCreate, ProductResponse
from services.product_service import *

router = APIRouter(tags=["Products"])

# CREATE
@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    return create_product_service(product)


# READ ALL
@router.get("/products", response_model=list[ProductResponse])
def get_products():
    return get_all_products_service()


# READ ONE
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    product = get_product_service(product_id)
    
    if product:
        return product
    
    return {"error": "Product not found"}


# UPDATE
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate):
    updated = update_product_service(product_id, product)
    
    if updated:
        return updated
    
    return {"error": "Product not found"}


# DELETE
@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    deleted = delete_product_service(product_id)
    
    if deleted:
        return {"message": "Product deleted"}
    
    return {"error": "Product not found"}