"""
main.py

Main entry point of the FastAPI application.
Defines API routes and initializes database.
"""

import logging

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, Base, get_db


# ---------------- Logging Configuration ---------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------- Database Initialization ---------------- #

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)


# ---------------- FastAPI App ---------------- #

app = FastAPI(
    title="Address Book API",
    description="API for managing addresses with geolocation",
    version="1.0"
)


# ---------------- Routes ---------------- #

@app.get("/")
def root():
    """
    Health check endpoint.
    """

    return {"message": "Address API running"}


@app.post("/addresses", response_model=schemas.AddressOut)
def create(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new address.
    """

    logger.info("Creating new address")

    return crud.create_address(db, address)


@app.get("/addresses", response_model=list[schemas.AddressOut])
def read_all(db: Session = Depends(get_db)):
    """
    Retrieve all stored addresses.
    """

    return crud.get_addresses(db)


@app.put("/addresses/{address_id}", response_model=schemas.AddressOut)
def update(
    address_id: int,
    address: schemas.AddressUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing address.
    """

    updated = crud.update_address(db, address_id, address)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    logger.info(f"Updated address {address_id}")

    return updated


@app.delete("/addresses/{address_id}")
def delete(
    address_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete address by ID.
    """

    deleted = crud.delete_address(db, address_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    logger.info(f"Deleted address {address_id}")

    return {"message": "Deleted"}


@app.get("/addresses/nearby")
def nearby(
    lat: float,
    lon: float,
    distance: float,
    db: Session = Depends(get_db)
):
    """
    Retrieve nearby addresses based on distance.
    """

    return crud.get_addresses_within_distance(
        db,
        lat,
        lon,
        distance
    )
