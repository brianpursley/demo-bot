from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
    product_name: str
    quantity_per_unit: str
    unit_price: float
    discontinued: bool
    units_in_stock: int
    category_id: int
    category_name: str


class Category(BaseModel):
    category_id: int
    category_name: str
    description: str