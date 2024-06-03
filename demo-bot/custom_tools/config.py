import os
import dotenv

dotenv.load_dotenv()

CATALOG_API_URL = os.getenv("CATALOG_API_URL")
CATALOG_API_TOKEN = os.getenv("CATALOG_API_TOKEN")

EMAIL_API_URL = os.getenv("EMAIL_API_URL")
EMAIL_API_TOKEN = os.getenv("EMAIL_API_TOKEN")
