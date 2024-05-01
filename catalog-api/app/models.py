from pydantic import BaseModel
from typing import Optional


class Category(BaseModel):
    id: Optional[int]
    name: str
    description: str


class Manufacturer(BaseModel):
    id: Optional[int]
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    category_id: int
    manufacturer_id: int
    quantity: int
    unit_price: float
