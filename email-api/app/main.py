from fastapi import FastAPI
from .routers import email
from .config import EMAIL_API_URL

# TODO: Implement Authentication

print(f"E-mail API URL: {EMAIL_API_URL}")

app = FastAPI(
    title="Email API",
    version="1.0.0",
    servers=[
        {"url": EMAIL_API_URL}
    ],
)
app.include_router(email.router)
