import json

from langchain_core.tools import tool
import os
import dotenv
import psycopg

dotenv.load_dotenv()
NORTHWIND_DATABASE_URL = os.getenv("NORTHWIND_DATABASE_URL")

northwind_conn = psycopg.connect(NORTHWIND_DATABASE_URL)


def fetchall_json(query, params=None):
    with northwind_conn.cursor() as c:
        c.execute(query, params)
        col_names = [desc[0] for desc in c.description]
        result = [dict(zip(col_names, row)) for row in c.fetchall()]
        return json.dumps(result, default=str)


def fetchone_json(query, params=None):
    with northwind_conn.cursor() as c:
        c.execute(query, params)
        col_names = [desc[0] for desc in c.description]
        row = c.fetchone()
        result = dict(zip(col_names, row)) if row else None
        return json.dumps(result, default=str) if result else None


@tool
def get_product_categories():
    """
    Get a list of all product categories.

    :return A JSON array of categories, including the following fields for each category: category_id, category_name.
    """
    return fetchall_json("""
        SELECT 
            category_id, 
            category_name
        FROM categories
        ORDER BY category_id;
    """)


@tool
def get_category_products(category_id):
    """
    Get a list of all products that belong to the specified category.

    :param category_id The category_id of the category for which you want to get the products.
    :return A JSON array of products, including the following fields for each product: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return fetchall_json("""
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
        WHERE c.category_id = %(category_id)s
        ORDER BY p.product_id;
    """, {"category_id": category_id})


@tool
def get_all_products():
    """
    Get a list of all products.

    :return A JSON array of products, including the following fields for each product: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return fetchall_json("""
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


@tool
def get_product(product_id):
    """
    Get a single product by its ID.

    :param product_id: The product_id of the product you want to get.
    :return A JSON object representing the product, including the following fields: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return fetchone_json("""
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
        WHERE p.product_id = %(product_id)s
        ORDER BY p.product_id
    """, {"product_id": product_id})


northwind_sql_tools = [
    get_product_categories,
    get_category_products,
    get_all_products,
    get_product
]
