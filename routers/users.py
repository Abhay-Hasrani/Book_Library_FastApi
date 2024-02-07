from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import users_controller
from controllers.auth_controller import get_current_user
from db.database import SessionLocal
from starlette import status

from schema.auth_schema import CreateUserRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(db: db_dependency, user: user_dependency):
    return users_controller.get_user(db,user)

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(db: db_dependency, user: user_dependency, user_id: int):
    return users_controller.get_user_by_id(db,user,user_id)

@router.get("/all",status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    return users_controller.get_all_users(db)

@router.post("/post-user", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    users_controller.create_user(db,create_user_request)