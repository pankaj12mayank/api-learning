from fastapi import FastAPI
from pydantic import BaseModel

class user(BaseModel):
    name: str
    age: int
    message: str

class userrepsonse(BaseModel):
    name:str
    message: str

app = FastAPI()

@app.post("/user",response_model= userrepsonse)
def create_user(user:user):
    return {
        "name": user.name,
        "age": user.age,
        "message": user.message

    }

class product(BaseModel):
    name: str
    model: str
    price: int

class product_response(BaseModel):
    name: str
    model: str


@app.post("/product", response_model=product_response)

def create_product(product:product):
        return{
            "name": product.name,
            "model": product.model,
            "price": product.price

        }



