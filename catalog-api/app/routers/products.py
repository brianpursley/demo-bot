from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models import Category, Manufacturer, Product
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
            ORDER BY p.id;
        """)


@router.get("/products/{id}", response_model=Product)
async def get_product(id: int, db=Depends(get_database)):
    """
    Get a product by its ID
    """
    product = await db.fetch_one(
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
            WHERE p.product_id = :id;
        """,
        values={"id": id})
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/products/{id}/category", response_model=Category)
async def get_product_category(id: int, db=Depends(get_database)):
    """
    Get Category for a specific Product
    """
    category = await db.fetch_one(
        query="""
            SELECT c.id, c.name, c.description
            FROM category AS c
            JOIN product AS p ON c.id = p.category_id
            WHERE p.id = :id;
        """,
        values={"id": id})
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found for this product")
    return category


@router.get("/products/{id}/manufacturer", response_model=Manufacturer)
async def get_product_manufacturer(id: int, db=Depends(get_database)):
    """
    Get Manufacturer for a specific Product
    """
    manufacturer = await db.fetch_one(
        query="""
            SELECT m.id, m.name, m.address, m.city, m.state, m.zip, m.email, m.phone
            FROM manufacturer AS m
            JOIN product AS p ON m.id = p.manufacturer_id
            WHERE p.id = :id;
        """,
        values={"id": id})
    if manufacturer is None:
        raise HTTPException(status_code=404, detail="Manufacturer not found for this product")
    return manufacturer
