from fastapi import HTTPException
from sqlalchemy.orm import Session
from helpers.enums import BookRequestStatus, UserRole
from starlette import status
from models.user_book import UserBook
from schema.book_schema import BookIssueRequest

def get_all_requests(db: Session, user: dict):
    return db.query(UserBook).all()

    
def generate_book_request(db: Session, user: dict, book_id: int):
    user_book_model = UserBook(user_id=user['id'], book_id=book_id, status=BookRequestStatus.PENDING)
    # user_model.books.append(user_book_model)
    db.add(user_book_model)
    db.commit()
    return {"message": "Book associated with user"}


def change_request_status(db: Session, user: dict, book_issue_request: BookIssueRequest):
    new_status = book_issue_request.status
    if (new_status==BookRequestStatus.ACCEPTED or new_status==BookRequestStatus.REJECTED) and user['role']!=UserRole.ADMIN:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED , detail='Authentication Failed: only Admins can accept reuqest')
    
    user_book_model = db.query(UserBook).filter(UserBook.book_id == book_issue_request.book_id, UserBook.user_id == user['id']).first()
    user_book_model.status = book_issue_request.status
    db.commit()