# app/controllers/user.py
from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/auth/me")
def read_all_book():
    return [{"book_id": 1}]

@router.post("/auth/me")
def post_book():
    return {"book_id": 1}

@router.put("/auth/me")
def put_book():
    return {"book_id": 1}

@router.delete("/auth/me")
def delete_book():
    return {"book_id": 1}