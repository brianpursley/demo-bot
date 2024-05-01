from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models import Category, Manufacturer, Product
from ..dependencies import get_database

router = APIRouter()


@router.get("/manufacturers", response_model=List[Manufacturer])
async def get_manufacturers(db=Depends(get_database)):
    """
    Get all manufacturers
    """
    return await db.fetch_all(
        query="""
            SELECT id, name, address, city, state, zip, email, phone
            FROM manufacturer
            ORDER BY name;
        """)


@router.get("/manufacturers/{id}", response_model=Manufacturer)
async def get_manufacturer(id: int, db=Depends(get_database)):
    """
    Get a manufacturer by its ID
    """
    manufacturer = await db.fetch_one(
        query="""
            SELECT id, name, address, city, state, zip, email, phone
            FROM manufacturer
            WHERE id = :id;
        """,
        values={"id": id})
    if manufacturer is None:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return manufacturer


@router.get("/manufacturers/{id}/categories", response_model=List[Category])
async def get_manufacturer_categories(id: int, db=Depends(get_database)):
    """
    Get all categories for a specific manufacturer
    """
    return await db.fetch_all(
        query="""
            SELECT DISTINCT c.id, c.name, c.description
            FROM category AS c
            JOIN product AS p ON c.id = p.category_id
            WHERE p.manufacturer_id = :id
            ORDER BY c.name;
        """,
        values={"id": id})


@router.get("/manufacturers/{id}/products", response_model=List[Product])
async def get_manufacturer_products(id: int, db=Depends(get_database)):
    """
    Get all products for a specific manufacturer
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
            WHERE p.manufacturer_id = :id
            ORDER BY p.id;
        """,
        values={"id": id})
