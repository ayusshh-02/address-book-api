"""
crud.py

This module contains all database-related business logic.
It isolates database operations from API routes, following
the separation of concerns principle.
"""

from sqlalchemy.orm import Session

from . import models, schemas
from .utils import calculate_distance


def create_address(db: Session, address: schemas.AddressCreate):
    """
    Create and persist a new address in the database.

    Args:
        db (Session): Active SQLAlchemy session.
        address (AddressCreate): Validated address input data.

    Returns:
        Address: Newly created database record.
    """

    # Convert Pydantic model to SQLAlchemy model
    db_address = models.Address(**address.dict())

    # Add to session (staged for commit)
    db.add(db_address)

    # Commit transaction (write to DB)
    db.commit()

    # Refresh object with DB-generated values (e.g., ID)
    db.refresh(db_address)

    return db_address


def get_addresses(db: Session):
    """
    Fetch all addresses from the database.

    Args:
        db (Session): Active database session.

    Returns:
        List[Address]: All address records.
    """

    return db.query(models.Address).all()


def update_address(db: Session, address_id: int, address: schemas.AddressUpdate):
    """
    Update an existing address.

    Args:
        db (Session): Database session.
        address_id (int): ID of the address to update.
        address (AddressUpdate): Updated field values.

    Returns:
        Address | None: Updated record or None if not found.
    """

    # Find record by ID
    db_address = (
        db.query(models.Address)
        .filter(models.Address.id == address_id)
        .first()
    )

    # If record does not exist
    if not db_address:
        return None

    # Update only fields provided by client
    for key, value in address.dict(exclude_unset=True).items():
        setattr(db_address, key, value)

    # Persist changes
    db.commit()
    db.refresh(db_address)

    return db_address


def delete_address(db: Session, address_id: int):
    """
    Delete an address by ID.

    Args:
        db (Session): Database session.
        address_id (int): ID of address to delete.

    Returns:
        Address | None: Deleted record or None if not found.
    """

    db_address = (
        db.query(models.Address)
        .filter(models.Address.id == address_id)
        .first()
    )

    if not db_address:
        return None

    db.delete(db_address)
    db.commit()

    return db_address


def get_addresses_within_distance(
    db: Session,
    lat: float,
    lon: float,
    distance: float
):
    """
    Retrieve all addresses within a given distance
    from a reference coordinate.

    Args:
        db (Session): Database session.
        lat (float): Reference latitude.
        lon (float): Reference longitude.
        distance (float): Max distance in kilometers.

    Returns:
        List[Address]: Addresses within distance.
    """

    # Fetch all records (can be optimized later)
    addresses = db.query(models.Address).all()

    result = []

    # Calculate distance for each address
    for addr in addresses:

        dist = calculate_distance(
            lat,
            lon,
            addr.latitude,
            addr.longitude
        )

        if dist <= distance:
            result.append(addr)

    return result
