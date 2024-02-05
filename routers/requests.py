from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import requests_controller
from controllers.auth_controller import get_current_user
from db.database import SessionLocal
from starlette import status
from schema.book_schema import BookIssueRequest


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_requests(db: db_dependency,user: user_dependency):
    return requests_controller.get_all_requests(db,user)

@router.post("/post-request", status_code=status.HTTP_201_CREATED)
async def generate_book_request(db: db_dependency , user: user_dependency, book_id: int):
    return requests_controller.generate_book_request(db,user,book_id)

@router.put("/put-request-status", status_code=status.HTTP_204_NO_CONTENT)
async def change_request_status(db: db_dependency, user: user_dependency, book_issue_request:BookIssueRequest):
    requests_controller.change_request_status(db,user,book_issue_request)