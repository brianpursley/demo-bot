import requests

from langchain_core.tools import tool
import os
import dotenv

dotenv.load_dotenv()
NORTHWIND_API_URL = os.getenv("NORTHWIND_API_URL")
NORTHWIND_API_TOKEN = os.getenv("NORTHWIND_API_TOKEN")


def api_get(url):
    response = requests.get(
        f"{NORTHWIND_API_URL}{url}",
        headers={"Authorization": f"Bearer {NORTHWIND_API_TOKEN}"}
    )
    return response.json()


@tool
def get_product_categories():
    """
    Get a list of all product categories.

    :return A JSON array of categories, including the following fields for each category: category_id, category_name.
    """
    return api_get("/categories")


@tool
def get_category_products(category_id):
    """
    Get a list of all products that belong to the specified category.

    :param category_id The category_id of the category for which you want to get the products.
    :return A JSON array of products, including the following fields for each product: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return api_get(f"/categories/{category_id}/products")


@tool
def get_all_products():
    """
    Get a list of all products.

    :return A JSON array of products, including the following fields for each product: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return api_get("/products")


@tool
def get_product(product_id):
    """
    Get a single product by its ID.

    :param product_id: The product_id of the product you want to get.
    :return A JSON object representing the product, including the following fields: product_id, product_name, quantity_per_unit, unit_price, discontinued, units_in_stock, category_id, category_name.
    """
    return api_get(f"/products/{product_id}")


northwind_api_tools = [
    get_product_categories,
    get_category_products,
    get_all_products,
    get_product
]
