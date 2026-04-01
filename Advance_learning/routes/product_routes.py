from fastapi import APIRouter
from models.product_model import Product
from services.product_service import *

router = APIRouter()

@router.post("/products")
def create_product(product: Product):
    return create_product_service(product)

@router.get("/products")
def get_products():
    return get_all_services()

@router.get("/products/{Product_id}")
def get_product(Product_id: int):
    product = get_product_service(Product_id)
    if product:
        return product
    return {"error": "Not found"}

@router.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    updated = update_product_services(product_id, product)
    if updated:
        return updated
    return {"error": "Not found"}

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    deleted = deleted_product_services(product_id)
    if deleted:
        return {"message": "Deleted"}
    return {"error": "Not found"}
