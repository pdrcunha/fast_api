from fastapi import FastAPI
from app.api import books, auth, rent_books, users_manager
from app.config import session
from dotenv import dotenv_values
config = dotenv_values("./.env") 

app = FastAPI()
app.include_router(books.router)
app.include_router(auth.router)
app.include_router(rent_books.router)
app.include_router(users_manager.router)

session.test_connection()