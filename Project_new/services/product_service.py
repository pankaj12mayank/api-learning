from database.db import SessionLocal
from models.product_model import Product

# CREATE
def create_product_service(product):
    db = SessionLocal()

    new_product = Product(
        id=product.id,
        pname=product.pname,
        price=product.price,
        qty=product.qty,
        meg=product.meg
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return new_product


# READ ALL
def get_all_products_service():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products


# READ ONE
def get_product_service(product_id):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    return product


# UPDATE
def update_product_service(product_id, updated_product):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        product.pname = updated_product.pname
        product.price = updated_product.price
        product.qty = updated_product.qty
        product.meg = updated_product.meg

        db.commit()
        db.refresh(product)
        db.close()
        return product

    db.close()
    return None


# DELETE
def delete_product_service(product_id):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        db.delete(product)
        db.commit()
        db.close()
        return True

    db.close()
    return False