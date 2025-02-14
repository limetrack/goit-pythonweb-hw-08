from fastapi import FastAPI
from database.db import Base, engine
from routers import contacts

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(contacts.router)
