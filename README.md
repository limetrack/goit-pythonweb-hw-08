# Contacts API
This is a RESTful API for managing contacts built with FastAPI and SQLAlchemy. It allows users to perform CRUD operations, search for contacts, and retrieve upcoming birthdays.

## Prerequisites
Python 3.10+, PostgreSQL database

## Installation
### Clone the repository:
```
git clone https://github.com/your-repo/goit-pythonweb-hw-08.git
cd goit-pythonweb-hw-08
```

### Install dependencies using Poetry:
```
poetry install
```

### Activate the virtual environment:
```
poetry shell
```

### Configure the database:
Set the DATABASE_URL environment variable or modify it in database.py.
Example:
```
DATABASE_URL=postgresql://user:password@localhost:5432/contacts_db
```

### Run the application:
```
uvicorn main:app --reload
```

## Usage
### Endpoints
POST /contacts/: Create a new contact.

GET /contacts/: Retrieve all contacts or search by name/email.

GET /contacts/{contact_id}: Retrieve a contact by ID.

PUT /contacts/{contact_id}: Update a contact by ID.

DELETE /contacts/{contact_id}: Delete a contact by ID.

GET /contacts/upcoming_birthdays/: Get contacts with upcoming birthdays in the next 7 days.

Example Contact JSON

```
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "birthday": "1990-01-01",
  "additional_info": "Some additional info"
}
```
