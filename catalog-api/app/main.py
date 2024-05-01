import os

import dotenv
from fastapi import FastAPI
from .routers import categories, manufacturers, products
from .dependencies import database

# TODO: Implement Authentication

dotenv.load_dotenv()
CATALOG_API_URL = os.getenv("CATALOG_API_URL")

app = FastAPI(
    title="Catalog API",
    version="1.0.0",
    servers=[
        {"url": CATALOG_API_URL}
    ],
)
app.include_router(categories.router)
app.include_router(manufacturers.router)
app.include_router(products.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
