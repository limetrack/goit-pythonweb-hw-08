from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, extract
from datetime import datetime, timedelta
from models.contact import Contact
from database.schemas.contact import ContactCreate


def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session, name: str = None, email: str = None):
    query = db.query(Contact)
    if name:
        query = query.filter(
            or_(
                Contact.first_name.ilike(f"%{name}%"),
                Contact.last_name.ilike(f"%{name}%"),
            )
        )
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))
    return query.all()


def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, contact: ContactCreate):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not db_contact:
        return None
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact


def get_upcoming_birthdays(db: Session):
    today = datetime.today().date()
    today_month = today.month
    today_day = today.day

    next_week = today + timedelta(days=7)
    next_week_month = next_week.month
    next_week_day = next_week.day

    return (
        db.query(Contact)
        .filter(
            and_(
                and_(
                    extract("month", Contact.birthday) == today_month,
                    extract("day", Contact.birthday) >= today_day,
                ),
                and_(
                    extract("month", Contact.birthday) == next_week_month,
                    extract("day", Contact.birthday) <= next_week_day,
                ),
            )
        )
        .all()
    )
