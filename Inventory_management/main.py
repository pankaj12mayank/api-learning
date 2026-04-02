from fastapi import FastAPI
from database.db import engine, Base
from routes.product_route import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Inventory management system"}

app.include_router(router, prefix="/api/v1")
