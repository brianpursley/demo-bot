import os
import dotenv

dotenv.load_dotenv()

CATALOG_API_URL = os.getenv("CATALOG_API_URL")
if not CATALOG_API_URL:
    raise ValueError("CATALOG_API_URL is not set")

CATALOG_DATABASE_URL = os.getenv("CATALOG_DATABASE_URL")
if not CATALOG_DATABASE_URL:
    raise ValueError("CATALOG_DATABASE_URL is not set")
