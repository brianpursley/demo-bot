import os
import dotenv
from databases import Database

dotenv.load_dotenv()
NORTHWIND_DATABASE_URL = os.getenv("NORTHWIND_DATABASE_URL")
database = Database(NORTHWIND_DATABASE_URL)


async def get_database():
    try:
        await database.connect()
        yield database
    finally:
        # No need to explicitly disconnect after each request,
        # as connections are managed by the pool.
        pass

