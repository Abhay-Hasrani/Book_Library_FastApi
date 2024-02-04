from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import books_controller
from db.database import SessionLocal
from starlette import status
from schema.book_schema import BookRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_books(db: db_dependency):
    return books_controller.get_all_books(db)

@router.get("/{book_id}",status_code=status.HTTP_200_OK)
async def get_book_by_id(db: db_dependency, book_id: int):
    return books_controller.get_book_by_id(db,book_id)


@router.post("/add-book", status_code=status.HTTP_201_CREATED)
async def add_book(db: db_dependency,book_request: BookRequest):
    books_controller.add_book(db,book_request)
    