import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from alembic import context
from app.models import Base  # Make sure this is imported correctly
from app.db import DATABASE_URL  # Update if needed to point to the correct DB URL

def run_migrations_online():
    # Get the database URL from environment variables
    connectable = create_async_engine(DATABASE_URL, echo=True)
    
    # Create a sessionmaker for asyncpg
    SessionLocal = sessionmaker(
        bind=connectable,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
    # Run the migration in an async context
    async def do_run_migrations():
        async with connectable.connect() as connection:
            # Make sure the migration is run in an async environment
            context.configure(
                connection=connection,
                target_metadata=Base.metadata,
                compare_type=True,
            )
            
            # Begin running migrations
            with context.begin_transaction():
                await context.run_migrations()

    asyncio.run(do_run_migrations())  # Use asyncio.run to run the async function
