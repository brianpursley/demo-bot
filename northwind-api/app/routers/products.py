from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models import Product
from ..dependencies import get_database

router = APIRouter()


@router.get("/products", response_model=List[Product])
async def get_products(db=Depends(get_database)):
    """
    Get all products
    """
    return await db.fetch_all(
        query="""
            SELECT 
                p.product_id, 
                p.product_name, 
                p.quantity_per_unit, 
                p.unit_price, 
                p.discontinued,
                p.units_in_stock,
                c.category_id,
                c.category_name
            FROM products p
            INNER JOIN categories c ON p.category_id = c.category_id 
            ORDER BY p.product_id
        """)


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int, db=Depends(get_database)):
    """
    Get a product by its ID
    """
    result = await db.fetch_one(
        query="""
            SELECT 
                p.product_id, 
                p.product_name, 
                p.quantity_per_unit, 
                p.unit_price, 
                p.discontinued,
                p.units_in_stock,
                c.category_id,
                c.category_name
            FROM products p
            INNER JOIN categories c ON p.category_id = c.category_id 
            WHERE p.product_id = :product_id
        """,
        values={"product_id": product_id})
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result
