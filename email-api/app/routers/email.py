import smtplib
from email.message import EmailMessage
from fastapi import APIRouter
from ..models import EmailRequest
from ..config import *

router = APIRouter()


@router.post("/email")
async def send_email(request: EmailRequest):
    msg = EmailMessage()
    msg['From'] = SMTP_FROM_EMAIL
    msg['To'] = request.to
    msg['Subject'] = request.subject
    msg.set_content(request.body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)
