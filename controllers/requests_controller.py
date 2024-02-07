from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from helpers.enums import BookRequestStatus, UserRole
from starlette import status
from helpers.model_to_json import json_book_join_request, json_book_request
from models.user import User
from models.user_book import UserBook
from schema.book_schema import BookIssueStatusRequest

def get_all_requests(db: Session, user: dict):
    query_result =  db.query(UserBook,User).join(UserBook).order_by(UserBook.created_at.desc()).all()

    result_json = []
    for user_book, user in query_result:
        result_dict = json_book_join_request(user_book,user)
        result_json.append(result_dict)
    
    return result_json

    
def generate_book_request(db: Session, user: dict, book_id: int):
        user_book_model = db.query(UserBook) \
            .filter(and_(UserBook.book_id == book_id , UserBook.user_id == user['id'] , UserBook.status == BookRequestStatus.PENDING)).first()

        if user_book_model:
            print(user_book_model.status)
            raise HTTPException(status_code= status.HTTP_409_CONFLICT , detail='Request already sent')
        
        user_book_model = UserBook(user_id=user['id'], book_id=book_id, status=str(BookRequestStatus.PENDING))
        db.add(user_book_model)
        db.commit()
        user_book = json_book_request(user_book_model)
        return {"user_book": user_book}


def change_request_status(db: Session, user: dict, book_issue_request: BookIssueStatusRequest):
    new_status = book_issue_request.status
    if (new_status==BookRequestStatus.ACCEPTED or new_status==BookRequestStatus.REJECTED) and user['role']!=UserRole.ADMIN:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED , detail='Authentication Failed: only Admins can accept reuqest')
    
    user_book_model = db.query(UserBook) \
        .filter(UserBook.book_id == book_issue_request.book_id, UserBook.user_id == book_issue_request.user_id) \
        .first()
    user_book_model.status = book_issue_request.status
    db.commit()
    user_book = json_book_request(user_book_model)
    return {"message":"Status updated Successfully","user_book":user_book}

def get_my_requests(db: Session, user: dict):
    return db.query(UserBook).filter(UserBook.user_id == user['id']).order_by(UserBook.created_at.desc()).all()