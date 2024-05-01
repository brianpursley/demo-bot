import requests

from langchain_core.tools import tool
import os
import dotenv

dotenv.load_dotenv()
CATALOG_API_URL = os.getenv("CATALOG_API_URL")
CATALOG_API_TOKEN = os.getenv("CATALOG_API_TOKEN")


def api_get(url):
    response = requests.get(
        f"{CATALOG_API_URL}{url}",
        headers={"Authorization": f"Bearer {CATALOG_API_TOKEN}"}
    )
    response.raise_for_status()
    return response.json()


@tool
def get_categories():
    """
    Get a list of all categories.

    :return A JSON array of categories, including the following fields for each category: id, name, description.
    """
    return api_get("/categories")


@tool
def get_category(category_id):
    """
    Get a single category by its ID.

    :param category_id: The integer ID of the category you want to get.
    :return A JSON object representing the category, including the following fields: id, name, description.
    """
    return api_get(f"/categories/{category_id}")


@tool
def get_category_manufacturers(category_id):
    """
    Get a list of all manufacturers that have any products in the specified category.

    :param category_id The integer ID of the category for which you want to get the manufacturers.
    :return A JSON array of manufacturers, including the following fields for each manufacturer: id, name, address, city, state, zip, email, phone.
    """
    return api_get(f"/categories/{category_id}/manufacturers")


@tool
def get_category_products(category_id):
    """
    Get a list of all products that belong to the specified category.

    :param category_id The integer ID of the category for which you want to get the products.
    :return A JSON array of products, including the following fields for each product: id, name, description, category_id, category_name, manufacturer_id, manufacturer_name, quantity, unit_price.
    """
    return api_get(f"/categories/{category_id}/products")


@tool
def get_manufacturers():
    """
    Get a list of all manufacturers.

    :return A JSON array of manufacturers, including the following fields for each manufacturer: id, name, address, city, state, zip, email, phone.
    """
    return api_get("/manufacturers")


@tool
def get_manufacturer(manufacturer_id):
    """
    Get a single manufacturer by its ID.

    :param manufacturer_id: The integer ID of the manufacturer you want to get.
    :return A JSON object representing the manufacturer, including the following fields: id, name, address, city, state, zip, email, phone.
    """
    return api_get(f"/manufacturers/{manufacturer_id}")


@tool
def get_manufacturer_categories(manufacturer_id):
    """
    Get a list of all categories that have any products from the specified manufacturer.

    :param manufacturer_id The integer ID of the manufacturer for which you want to get the categories.
    :return A JSON array of categories, including the following fields for each category: id, name, description.
    """
    return api_get(f"/manufacturers/{manufacturer_id}/categories")


@tool
def get_manufacturer_products(manufacturer_id):
    """
    Get a list of all products that belong to the specified manufacturer.

    :param manufacturer_id The integer ID of the manufacturer for which you want to get the products.
    :return A JSON array of products, including the following fields for each product: id, name, description, category_id, category_name, manufacturer_id, manufacturer_name, quantity, unit_price.
    """
    return api_get(f"/manufacturers/{manufacturer_id}/products")


@tool
def get_products():
    """
    Get a list of all products.

    :return A JSON array of products, including the following fields for each product: id, name, description, category_id, category_name, manufacturer_id, manufacturer_name, quantity, unit_price.
    """
    return api_get("/products")


@tool
def get_product(product_id):
    """
    Get a single product by its ID.

    :param product_id: The integer ID of the product you want to get.
    :return A JSON object representing the product, including the following fields: id, name, description, category_id, category_name, manufacturer_id, manufacturer_name, quantity, unit_price.
    """
    return api_get(f"/products/{product_id}")


@tool
def get_product_category(product_id):
    """
    Get the category for a specific product.

    :param product_id: The integer ID of the product for which you want to get the category.
    :return A JSON object representing the category of the product, including the following fields: id, name, description.
    """
    return api_get(f"/products/{product_id}/category")


@tool
def get_product_manufacturer(product_id):
    """
    Get the manufacturer for a specific product.

    :param product_id: The integer ID of the product for which you want to get the manufacturer.
    :return A JSON object representing the manufacturer of the product, including the following fields: id, name, address, city, state, zip, email, phone.
    """
    return api_get(f"/products/{product_id}/manufacturer")


catalog_api_tools = [
    get_categories,
    get_category,
    get_category_manufacturers,
    get_category_products,
    get_manufacturers,
    get_manufacturer,
    get_manufacturer_categories,
    get_manufacturer_products,
    get_products,
    get_product,
    get_product_category,
    get_product_manufacturer,
]
