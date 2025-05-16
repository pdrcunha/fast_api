# app/controllers/user.py
from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/rent-books/param")
def read_book(params: Union[str, None] = None):
    return {"rent_id": params}

@router.get("/rent-books")
def read_all_book():
    return [{"book_id": 1}]

@router.post("/rent-books")
def post_book():
    return {"book_id": 1}

@router.put("/rent-books")
def put_book():
    return {"book_id": 1}

@router.delete("/rent-books")
def delete_book():
    return {"book_id": 1}