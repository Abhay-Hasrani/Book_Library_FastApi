from fastapi import HTTPException
from sqlalchemy.orm import Session
from controllers.users_controller import get_user
from helpers.enums import BookRequestStatus, UserRole
from models.book import Book
from starlette import status
from models.user_book import UserBook
from schema.book_schema import BookIssueRequest, BookRequest

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    book_model = db.query(Book).filter(Book.id == book_id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found.')

def add_book(db: Session, book_request:BookRequest):
    todo_model = Book(**book_request.model_dump())
    db.add(todo_model)
    db.commit()
    return {"message": "Book added Successfully"}
    
def generate_book_request(db: Session, user: dict, book_id: int):
    user_book_model = UserBook(user_id=user['id'], book_id=book_id, status=BookRequestStatus.PENDING)
    # user_model.books.append(user_book_model)
    db.add(user_book_model)
    db.commit()
    return {"message": "Book associated with user"}

def get_all_requests(db: Session, user: dict):
    return db.query(UserBook).all()

def change_request_status(db: Session, user: dict, book_issue_request: BookIssueRequest):
    new_status = book_issue_request.status
    if (new_status==BookRequestStatus.ACCEPTED or new_status==BookRequestStatus.REJECTED) and user['role']!=UserRole.ADMIN:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED , detail='Authentication Failed: only Admins can accept reuqest')
    
    user_book_model = db.query(UserBook).filter(UserBook.book_id == book_issue_request.book_id, UserBook.user_id == user['id']).first()
    user_book_model.status = book_issue_request.status
    db.commit()