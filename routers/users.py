from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import users_controller
from db.database import SessionLocal
from starlette import status

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    return users_controller.get_all_users(db)

@router.get("/{user_id}",status_code=status.HTTP_200_OK)
async def get_user_by_id(db: db_dependency, user_id: int):
    return users_controller.get_user_by_id(db,user_id)