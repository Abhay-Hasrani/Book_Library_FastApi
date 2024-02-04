from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from models.user import User

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')