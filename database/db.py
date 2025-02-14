from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg2://user:pwd@localhost:5432/contacts_db"
)

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except OperationalError as e:
    print(f"Error connecting to the database: {e}")
