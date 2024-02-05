from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from controllers import auth_controller
from db.database import SessionLocal
from schema.auth_schema import CustomOAuth2PasswordRequestForm, Token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/token",response_model=Token)
async def login_for_access_token(db: db_dependency,form_data: CustomOAuth2PasswordRequestForm):
    return auth_controller.login_for_access_token(db,form_data)