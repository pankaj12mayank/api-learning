from itertools import product
from models.product_model import ProductDB
from database.db import SessionLocal

def create_product_services(product):
    db = SessionLocal()
    new_product = ProductDB(
        name=product.name,
        price=product.price,
        quantity=product.quantity,
        category=product.category
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    db.close()
    return new_product

def get_product_services():
    db = SessionLocal()
    return db.query(ProductDB).all()
    db.close()
    return products

def get_product_by_id_services(product_id):
    db = SessionLocal()
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    db.close()
    return product

def updated_product_services(product_id, updated_product):
    db = SessionLocal()
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()

    if product:
        product.name = updated_product.name
        product.price = updated_product.price
        product.quantity = updated_product.quantity
        product.category = updated_product.category

        db.commit()
        db.refresh(product)
        db.close()

        return product

    db.close ()
    return {"message": "product not found"}



def delete_product_services(product_id):
    db = SessionLocal()
    db.query(ProductDB).filter(ProductDB.id == product_id).delete()
    db.commit()
    db.close()
    return {"message": "Product deleted successfully"}