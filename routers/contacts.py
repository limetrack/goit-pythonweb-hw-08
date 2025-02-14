from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import List
from database.schemas.contact import ContactCreate, ContactResponse
from handlers.contacts import (
    create_contact,
    get_contacts,
    get_contact_by_id,
    update_contact,
    delete_contact,
    get_upcoming_birthdays,
)
from dependencies import get_db

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.post("/", response_model=ContactResponse)
def create_contact_route(contact: ContactCreate, db: Session = Depends(get_db)):
    try:
        return create_contact(db, contact)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[ContactResponse])
def get_contacts_route(
    name: str = Query(None), email: str = Query(None), db: Session = Depends(get_db)
):
    return get_contacts(db, name, email)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact_route(contact_id: int, db: Session = Depends(get_db)):
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
def update_contact_route(
    contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)
):
    updated_contact = update_contact(db, contact_id, contact)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact


@router.delete("/{contact_id}", response_model=dict)
def delete_contact_route(contact_id: int, db: Session = Depends(get_db)):
    deleted_contact = delete_contact(db, contact_id)
    if not deleted_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"detail": "Contact deleted successfully"}


@router.get("/upcoming_birthdays/", response_model=List[ContactResponse])
def get_upcoming_birthdays_route(db: Session = Depends(get_db)):
    return get_upcoming_birthdays(db)
