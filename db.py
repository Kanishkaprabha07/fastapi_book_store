import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# For SQLAlchemy setup, you may want to define your engine, session, and connection code here.
# Example using SQLAlchemy
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare base class for models
Base = declarative_base()

# To use this engine, you can now import `SessionLocal` and `engine` in other parts of your app
