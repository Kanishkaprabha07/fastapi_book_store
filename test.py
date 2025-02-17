from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

async def test_db_connection():
    # Your actual database URL, update this if necessary
    DATABASE_URL = "postgresql+asyncpg://avnadmin:AVNS_w3wZO5vqRzgkJrdLQQV@pg-3d2ee583-steinnlabs-90b8.h.aivencloud.com:25995/defaultdb?sslmode=require"

    # Create an async engine to test the connection
    engine = create_async_engine(DATABASE_URL, echo=True)

    # Establish the connection and ping the database
    async with engine.connect() as connection:
        result = await connection.execute("SELECT 1")
        print(result.scalar())  # Should print 1 if connection is successful

    # Close the engine connection after use
    await engine.dispose()

# Run the test
asyncio.run(test_db_connection())
