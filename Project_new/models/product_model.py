from sqlalchemy import Column, Integer, String
from database.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    pname = Column(String)
    price = Column(Integer)
    qty = Column(Integer)
    meg = Column(String)