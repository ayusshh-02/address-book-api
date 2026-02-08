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

## 📁 Project Structure

```
address-book-api/
│
├── app/
│   ├── main.py        # Application entry point
│   ├── database.py    # Database configuration
│   ├── models.py      # Database models
│   ├── schemas.py     # Request/response validation
│   ├── crud.py        # Database operations
│   ├── utils.py       # Utility functions
│
├── logs/              # Application logs
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── .gitignore         # Git ignore rules
```


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

