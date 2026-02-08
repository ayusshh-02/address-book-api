"""
database.py

Handles database configuration and session management.
Provides a reusable database dependency for FastAPI.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLite database URL
DATABASE_URL = "sqlite:///./addresses.db"


# Create SQLAlchemy engine (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for FastAPI threading
)


# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for ORM models
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session.

    Ensures that:
    - Session is opened per request
    - Session is closed after request

    Yields:
        Session: SQLAlchemy session
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        # Always close connection
        db.close()
