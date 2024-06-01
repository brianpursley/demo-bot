from databases import Database
from .config import CATALOG_DATABASE_URL

print(CATALOG_DATABASE_URL)
database = Database(CATALOG_DATABASE_URL)


async def get_database():
    try:
        await database.connect()
        yield database
    finally:
        # No need to explicitly disconnect after each request,
        # as connections are managed by the pool.
        pass

