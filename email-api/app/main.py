import os
import smtplib
import dotenv
from email.message import EmailMessage
from pydantic import BaseModel
from fastapi import FastAPI

# TODO: Implement Authentication

dotenv.load_dotenv()
EMAIL_API_URL = os.getenv("EMAIL_API_URL")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL")

print(f"E-mail API URL: {EMAIL_API_URL}")

app = FastAPI(
    title="Email API",
    version="1.0.0",
    servers=[
        {"url": EMAIL_API_URL}
    ],
)


class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str


@app.post("/email")
async def send_email(request: EmailRequest):
    msg = EmailMessage()
    msg['From'] = SMTP_FROM_EMAIL
    msg['To'] = request.to
    msg['Subject'] = request.subject
    msg.set_content(request.body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)
