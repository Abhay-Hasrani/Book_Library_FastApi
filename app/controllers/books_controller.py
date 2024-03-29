from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.helpers.model_to_json import json_book
from app.models.book import Book
from starlette import status
from app.schema.book_schema import BookRequest

def get_all_books(db: Session):
    return db.query(Book).order_by(Book.created_at.desc()).all()

def get_book_by_id(db: Session, book_id: int):
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found.')

def add_book(db: Session, book_request:BookRequest):
    book_model = Book(**book_request.model_dump())
    db.add(book_model)
    db.commit()
    book = json_book(book_model)
    return {"message": "Book added Successfully","book" : book}
