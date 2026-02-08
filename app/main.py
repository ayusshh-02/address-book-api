"""
main.py

Main entry point of the FastAPI application.
Configures logging, initializes the database,
and defines all API routes.
"""

import os
import logging

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import engine, Base, get_db


# ------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),   # File logging
        logging.StreamHandler()                # Console logging
    ]
)

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Database Initialization
# ------------------------------------------------------------------

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)


# ------------------------------------------------------------------
# FastAPI Application
# ------------------------------------------------------------------

app = FastAPI(
    title="Address Book API",
    description="REST API for managing addresses with geolocation",
    version="1.0"
)


# ------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------

@app.get("/")
def root():
    """
    Health check endpoint.
    """

    logger.info("Health check endpoint called")

    return {"message": "Address API running"}


@app.post("/addresses", response_model=schemas.AddressOut)
def create_address(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new address record.
    """

    logger.info("Creating new address: %s", address.name)

    return crud.create_address(db, address)


@app.get("/addresses", response_model=list[schemas.AddressOut])
def get_all_addresses(db: Session = Depends(get_db)):
    """
    Retrieve all addresses.
    """

    logger.info("Fetching all addresses")

    return crud.get_addresses(db)


@app.put("/addresses/{address_id}", response_model=schemas.AddressOut)
def update_address(
    address_id: int,
    address: schemas.AddressUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing address.
    """

    logger.info("Updating address with ID: %s", address_id)

    updated = crud.update_address(db, address_id, address)

    if not updated:
        logger.warning("Address not found for update: %s", address_id)

        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    logger.info("Address updated successfully: %s", address_id)

    return updated


@app.delete("/addresses/{address_id}")
def delete_address(
    address_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an address.
    """

    logger.info("Deleting address with ID: %s", address_id)

    deleted = crud.delete_address(db, address_id)

    if not deleted:
        logger.warning("Address not found for deletion: %s", address_id)

        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    logger.info("Address deleted successfully: %s", address_id)

    return {"message": "Deleted successfully"}


@app.get("/addresses/nearby", response_model=list[schemas.AddressOut])
def get_nearby_addresses(
    lat: float,
    lon: float,
    distance: float,
    db: Session = Depends(get_db)
):
    """
    Retrieve addresses within a given distance.
    """

    logger.info(
        "Searching nearby addresses | lat=%s lon=%s distance=%s",
        lat,
        lon,
        distance
    )

    results = crud.get_addresses_within_distance(
        db,
        lat,
        lon,
        distance
    )

    logger.info("Nearby search returned %s records", len(results))

    return results
