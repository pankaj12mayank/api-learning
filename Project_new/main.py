from fastapi import FastAPI
from database.db import engine, Base
from routes.product_routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)   # ✅ create table

app.include_router(router, prefix="/api/v1")