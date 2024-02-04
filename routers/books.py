from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import books_controller
from db.database import SessionLocal
from starlette import status
from schema.book_schema import BookIssueRequest, BookRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user():
    return {'username': 'abhay', 'id': 1, 'role': 'Student'}

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_books(db: db_dependency):
    return books_controller.get_all_books(db)

@router.get("/all-requests", status_code=status.HTTP_200_OK)
async def get_all_requests(db: db_dependency,user: user_dependency):
    return books_controller.get_all_requests(db,user)

@router.get("/{book_id}",status_code=status.HTTP_200_OK)
async def get_book_by_id(db: db_dependency, book_id: int):
    return books_controller.get_book_by_id(db,book_id)


@router.post("/add-book", status_code=status.HTTP_201_CREATED)
async def add_book(db: db_dependency, book_request: BookRequest):
    return books_controller.add_book(db,book_request)

@router.post("/request-book", status_code=status.HTTP_201_CREATED)
async def generate_book_request(db: db_dependency , user: user_dependency, book_id: int):
    return books_controller.generate_book_request(db,user,book_id)

@router.put("/change-book-request", status_code=status.HTTP_204_NO_CONTENT)
async def change_request_status(db: db_dependency, user: user_dependency, book_issue_request:BookIssueRequest):
    books_controller.change_request_status(db,user,book_issue_request)