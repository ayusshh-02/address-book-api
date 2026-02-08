"""
schemas.py

Defines Pydantic models for request validation
and response serialization.
"""

from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    """
    Schema for creating an address.
    """

    name: str = Field(..., min_length=2)
    street: str
    city: str
    latitude: float
    longitude: float


class AddressUpdate(BaseModel):
    """
    Schema for updating an address.
    All fields are optional.
    """

    name: str | None = None
    street: str | None = None
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class AddressOut(BaseModel):
    """
    Schema for API responses.
    """

    id: int
    name: str
    street: str
    city: str
    latitude: float
    longitude: float

    class Config:
        # Enable ORM compatibility
        from_attributes = True
