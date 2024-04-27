from fastapi import FastAPI
from .routers import categories, products
from .dependencies import database

app = FastAPI(
    title="Northwind API",
    version="1.0.0",
    servers=[
        {"url": "http://localhost:8000"}
    ],
)
app.include_router(categories.router)
app.include_router(products.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
