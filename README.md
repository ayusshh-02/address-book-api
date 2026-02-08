# Address Book API

A RESTful Address Book application built using **FastAPI** and **SQLite**.  
This API allows users to create, update, delete, and search addresses using geographic coordinates.

The project demonstrates clean architecture, validation, logging, and best practices in Python API development.

---

## Features

- Create, update, delete, and retrieve addresses
- Store latitude and longitude coordinates
- SQLite database using SQLAlchemy ORM
- Input validation using Pydantic
- Search addresses within a given distance
- Built-in Swagger documentation
- Logging support
- Modular and maintainable code structure

---

## Tech Stack

- **Python 3.9+**
- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Database
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

---

## Project Structure

address-book-api/ │ ├── app/ │ ├── main.py │ ├── database.py │ ├──
models.py │ ├── schemas.py │ ├── crud.py │ ├── utils.py │ ├── logs/ ├──
requirements.txt └── README.md

------------------------------------------------------------------------

## Installation

### Clone

git clone https://github.com/ayusshh-02/address-book-api.git cd
address-book-api

### Setup

python -m venv venv source venv/bin/activate

### Install

pip install -r requirements.txt

### Run

uvicorn app.main:app --reload

------------------------------------------------------------------------

## API Docs

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Endpoints

POST /addresses\
GET /addresses\
PUT /addresses/{id}\
DELETE /addresses/{id}

GET /addresses/nearby

------------------------------------------------------------------------

## Nearby Search Example

/addresses/nearby?lat=28.6&lon=77.2&distance=5

