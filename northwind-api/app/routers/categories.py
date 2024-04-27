from fastapi import APIRouter, Depends
from typing import List
from ..models import Category, Product
from ..dependencies import get_database

router = APIRouter()


@router.get("/categories", response_model=List[Category])
async def get_categories(db=Depends(get_database)):
    """
    Get all categories
    """
    return await db.fetch_all(
        query="""
            SELECT 
                category_id,
                category_name,
                description
            FROM categories 
            ORDER BY category_id
        """)


@router.get("/categories/{category_id}/products", response_model=List[Product])
async def get_category_products(category_id: int, db=Depends(get_database)):
    """
    Get all products for a specific category
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
            WHERE c.category_id = :category_id
            ORDER BY p.product_id
        """,
        values={"category_id": category_id})
