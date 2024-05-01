from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models import Category, Manufacturer, Product
from ..dependencies import get_database

router = APIRouter()


@router.get("/categories", response_model=List[Category])
async def get_categories(db=Depends(get_database)):
    """
    Get all categories
    """
    return await db.fetch_all(
        query="""
            SELECT id, name, description
            FROM category 
            ORDER BY id;
        """)


@router.get("/categories/{id}", response_model=Category)
async def get_category(db=Depends(get_database)):
    """
    Get a category by its ID
    """
    category = await db.fetch_all(
        query="""
            SELECT id, name, description
            FROM category 
            WHERE id = :id
            ORDER BY id;
        """,
        values={"id": id})
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/categories/{id}/manufacturers", response_model=List[Manufacturer])
async def get_category_manufacturers(id: int, db=Depends(get_database)):
    """
    Get all manufacturers for a specific category
    """
    return await db.fetch_all(
        query="""
            SELECT DISTINCT m.id, m.name, m.address, m.city, m.state, m.zip, m.email, m.phone
            FROM manufacturer AS m
            JOIN product AS p ON m.id = p.manufacturer_id
            WHERE p.category_id = :id
            ORDER BY m.name;
        """,
        values={"id": id})


@router.get("/categories/{id}/products", response_model=List[Product])
async def get_category_products(id: int, db=Depends(get_database)):
    """
    Get all products for a specific category
    """
    return await db.fetch_all(
        query="""
            SELECT 
                p.id,
                p.name,
                p.description,
                p.category_id,
                c.name AS category_name,
                p.manufacturer_id,
                m.name AS manufacturer_name,
                p.quantity,
                p.unit_price
            FROM product AS p
            JOIN category AS c ON p.category_id = c.id
            JOIN manufacturer AS m ON p.manufacturer_id = m.id
            WHERE p.category_id = :id
            ORDER BY p.id;
        """,
        values={"id": id})
