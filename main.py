from ast import Str
import sre_compile
from unicodedata import category
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Create App Instance
@app.get("/Pankaj")
def get_name():
    return {"name": "Pankaj"}

#First Endpoint (Route)
@app.get("/")
def home():
    return {"message": "Hello, API is working"}

#Second Endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello Pankaj 👋"}

#Path Parameters
@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {"user_id": user_id}

#Query Parameters (Filtering Data)
@app.get('/search')
def search_user(name: str, age: int, city: str):
    return {"name":name, "age":age, "city":city}


#Combine Both (Very Important)
@app.get('/users/{user_id}/details')
def user_details(user_id: int, active: bool = True):
    return {
        "user_id": user_id,
        "active": active
    }

#Default Values (Optional Params)

@app.get('/products')
def get_products(category: str = "none"):
    return {"category": category}


#Pydantic Model (Data Structure)

# Define data structure
class create_user(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(create_user: create_user):
    return {
        "message": "User created successfully",
        "data": create_user
    }


class create_product(BaseModel):
    category: str
    price: int

@app.post("/create_product")

def create_product(create_product: create_product):
    return {
        "message": "Product has been created",
        "data": create_product
    }