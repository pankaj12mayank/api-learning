from models.product_model import ProductDB
from fastapi import HTTPException

# ✅ CREATE
def create_product_service(product, db):
    new_product = ProductDB(
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category=product.category
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

# ✅ GET ALL
def get_products_service(db):
    return db.query(ProductDB).all()


# ✅ GET BY ID
def get_product_service(product_id, db):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# ✅ UPDATE
def update_product_service(product_id, updated_product, db):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # update fields
    product.name = updated_product.name
    product.price = updated_product.price
    product.quantity = updated_product.quantity
    product.category = updated_product.category

    db.commit()
    db.refresh(product)

    return product

# ✅ DELETE
def delete_product_service(product_id, db):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}