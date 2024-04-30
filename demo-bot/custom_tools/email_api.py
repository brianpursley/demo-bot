import requests

from langchain_core.tools import tool
import os
import dotenv

dotenv.load_dotenv()
EMAIL_API_URL = os.getenv("EMAIL_API_URL")
EMAIL_API_TOKEN = os.getenv("EMAIL_API_TOKEN")


@tool
def send_email(to, subject, body):
    """
    Sends an email to the specified recipient, with the specified subject and body.
    """
    response = requests.post(
        f"{EMAIL_API_URL}/email",
        json={"to": to, "subject": subject, "body": body},
        headers={"Authorization": f"Bearer {EMAIL_API_TOKEN}"}
    )
    response.raise_for_status()


email_api_tools = [
    send_email
]
