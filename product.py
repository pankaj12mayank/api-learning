from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model (PascalCase best practice)
class Product(BaseModel):
    id: int
    pname: str
    price: int
    qty: int
    meg: str

# Fake DB
product_DB = []

#api test
@app.get("/")
def home():
    return {"message": "API working"}

# CREATE
@app.post("/product")
def create_product(product: Product):
    product_DB.append(product)   # ✅ fixed
    return {"message": "Product has been added", "data": product}

# READ ALL
@app.get("/product")
def get_products():
    return product_DB

# READ ONE
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for p in product_DB:   # ✅ fixed loop
        if p.id == product_id:   # ✅ correct comparison
            return p
    return {"error": "Product Not Found"}

# UPDATE
@app.put("/product/{product_id}")
def update_product(product_id: int, updated_product: Product):   # ✅ fixed type
    for index, p in enumerate(product_DB):
        if p.id == product_id:   # ✅ correct comparison
            product_DB[index] = updated_product
            return {"message": "Product has been updated", "data": updated_product}
    return {"error": "Product not found"}

# DELETE
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    for index, p in enumerate(product_DB):
        if p.id == product_id:   # ✅ correct comparison
            product_DB.pop(index)   # ✅ fixed pop
            return {"message": "Product deleted"}
    return {"error": "Product not found"}