import requests

from .config import CATALOG_API_URL, CATALOG_API_TOKEN


def __api_get(url):
    response = requests.get(
        f"{CATALOG_API_URL}{url}",
        headers={"Authorization": f"Bearer {CATALOG_API_TOKEN}"}
    )
    response.raise_for_status()
    return response.json()


def get_categories(): return __api_get("/categories")
def get_category(category_id): return __api_get(f"/categories/{category_id}")
def get_category_manufacturers(category_id): return __api_get(f"/categories/{category_id}/manufacturers")
def get_category_products(category_id): return __api_get(f"/categories/{category_id}/products")
def get_manufacturers(): return __api_get("/manufacturers")
def get_manufacturer(manufacturer_id): return __api_get(f"/manufacturers/{manufacturer_id}")
def get_manufacturer_categories(manufacturer_id): return __api_get(f"/manufacturers/{manufacturer_id}/categories")
def get_manufacturer_products(manufacturer_id): return __api_get(f"/manufacturers/{manufacturer_id}/products")
def get_products(): return __api_get("/products")
def get_product(product_id): return __api_get(f"/products/{product_id}")
def get_product_category(product_id): return __api_get(f"/products/{product_id}/category")
def get_product_manufacturer(product_id): return __api_get(f"/products/{product_id}/manufacturer")


tools = [
    {
        "type": "function",
        "function": {
            "name": get_categories.__name__,
            "description": "Get a list of all categories.",
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_category.__name__,
            "description": "Get a single category by its ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category_id": {
                        "type": "number",
                        "description": "The ID of the category you want to get."
                    },
                },
                "required": ["category_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_category_manufacturers.__name__,
            "description": "Get a list of all manufacturers that have any products in the specified category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category_id": {
                        "type": "number",
                        "description": "The ID of the category for which you want to get the manufacturers."
                    },
                },
                "required": ["category_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_category_products.__name__,
            "description": "Get a list of all products that belong to the specified category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category_id": {
                        "type": "number",
                        "description": "The ID of the category for which you want to get the products."
                    },
                },
                "required": ["category_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_manufacturers.__name__,
            "description": "Get a list of all manufacturers.",
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_manufacturer.__name__,
            "description": "Get a single manufacturer by its ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "manufacturer_id": {
                        "type": "number",
                        "description": "The ID of the manufacturer you want to get."
                    },
                },
                "required": ["manufacturer_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_manufacturer_categories.__name__,
            "description": "Get a list of all categories that have any products from the specified manufacturer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "manufacturer_id": {
                        "type": "number",
                        "description": "The ID of the manufacturer for which you want to get the categories"
                    },
                },
                "required": ["manufacturer_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_manufacturer_products.__name__,
            "description": "Get a list of all products that have any products from the specified manufacturer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "manufacturer_id": {
                        "type": "number",
                        "description": "The ID of the manufacturer for which you want to get the products"
                    },
                },
                "required": ["manufacturer_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_products.__name__,
            "description": "Get a list of all products.",
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_product.__name__,
            "description": "Get a single product by its ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "number",
                        "description": "The ID of the product you want to get."
                    },
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_product_category.__name__,
            "description": "Get the category for a specific product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "number",
                        "description": "The ID of the product for which you want to get the category."
                    },
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": get_product_manufacturer.__name__,
            "description": "Get the manufacturer for a specific product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "number",
                        "description": "The ID of the product for which you want to get the manufacturer."
                    },
                },
                "required": ["product_id"]
            }
        }
    },
]
