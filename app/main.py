from fastapi import FastAPI
from app.api import books
from app.config import session
from dotenv import dotenv_values
config = dotenv_values("./.env") 

app = FastAPI()
app.include_router(books.router)

session.test_connection()