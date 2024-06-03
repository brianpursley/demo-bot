import os
import dotenv

dotenv.load_dotenv()

EMAIL_API_URL = os.getenv("EMAIL_API_URL")
if not EMAIL_API_URL:
    raise ValueError("EMAIL_API_URL is not set")

SMTP_SERVER = os.getenv("SMTP_SERVER")
if not SMTP_SERVER:
    raise ValueError("SMTP_SERVER is not set")

SMTP_PORT = int(os.getenv("SMTP_PORT"))
if not SMTP_PORT:
    raise ValueError("SMTP_PORT is not set")

SMTP_USERNAME = os.getenv("SMTP_USERNAME")
if not SMTP_USERNAME:
    raise ValueError("SMTP_USERNAME is not set")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
if not SMTP_PASSWORD:
    raise ValueError("SMTP_PASSWORD is not set")

SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL")
if not SMTP_FROM_EMAIL:
    raise ValueError("SMTP_FROM_EMAIL is not set")
