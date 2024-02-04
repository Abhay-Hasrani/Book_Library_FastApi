from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.book import Book
from starlette import status
from schema.book_schema import BookRequest

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found.')

def add_book(db: Session,book_request:BookRequest):
    todo_model = Book(**book_request.model_dump())
    db.add(todo_model)
    db.commit()
    