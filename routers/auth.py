from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from controllers import auth_controller
from db.database import SessionLocal
from schema.auth_schema import Token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/token",response_model=Token)
async def login_for_access_token(db: db_dependency,form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return auth_controller.login_for_access_token(db,form_data)