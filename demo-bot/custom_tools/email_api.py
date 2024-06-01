import requests

from .config import EMAIL_API_URL, EMAIL_API_TOKEN


def send_email(to, subject, body):
    response = requests.post(
        f"{EMAIL_API_URL}/email",
        json={"to": to, "subject": subject, "body": body},
        headers={"Authorization": f"Bearer {EMAIL_API_TOKEN}"}
    )
    response.raise_for_status()
    return {
        "result": "Email sent successfully."
    }


tools = [
    {
        "type": "function",
        "function": {
            "name": send_email.__name__,
            "description": "Sends an email.",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string",
                        "description": "The recipient email address."
                    },
                    "subject": {
                        "type": "string",
                        "description": "The email subject."
                    },
                    "body": {
                        "type": "string",
                        "description": "The email body."
                    }
                },
                "required": ["to", "subject", "body"]
            }
        }
    },
]