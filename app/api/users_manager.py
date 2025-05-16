# app/controllers/user.py
from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/users/param")
def read_book(params: Union[str, None] = None):
    return {"users_id": params}

@router.get("/users")
def read_all_book():
    return [{"book_id": 1}]
