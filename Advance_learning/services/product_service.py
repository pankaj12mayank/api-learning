from database.db import Product_DB

def create_product_service(Product):
    Product_DB.append(Product)
    return {"message":"Product created", "data": Product}

def get_all_services():
    return {"message":"All products", "data": Product_DB}

def get_product_service(Product_id):
    for p in Product_DB:
        if p.id == Product_id:
            return {"message":"Product found", "data": p}
    return {"message":"Product not found", "data": None}

def update_product_services(Product_id, Updated_product):
    for index, p in enumerate (Product_DB):
        if p.id == Product_id:
            Product_DB[index] = Updated_product
            return {"message":"Product updated", "data": Updated_product}
    return {"message":"Product not found", "data": None}


def deleted_product_services(product_id):
    for index, p in enumerate (Product_DB):
        if p.id == product_id:
            Product_DB.pop(index)
            return {"message":"Product deleted", "data": True}
    return {"message":"Product not found", "data": None}

