# app/controllers/user.py
from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/books/param")
def read_book(params: Union[str, None] = None):
    return {"books_id": params}

@router.get("/books")
def read_all_book():
    return [{"book_id": 1}]

@router.post("/books")
def post_book():
    return {"book_id": 1}

@router.put("/books")
def put_book():
    return {"book_id": 1}

@router.delete("/books")
def delete_book():
    return {"book_id": 1}