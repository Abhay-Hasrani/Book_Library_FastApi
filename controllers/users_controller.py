from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from models.user import User
from schema.auth_schema import CreateUserRequest
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, create_user_request: CreateUserRequest):
    create_user_model = User(
        email = create_user_request.email,
        username = create_user_request.username,
        role = create_user_request.role,
        hashed_password = bcrypt_context.hash(create_user_request.password)
    )
    
    db.add(create_user_model)
    db.commit()
    
    
def get_user(db: Session,user: dict):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(User).filter(User.id == user.get('id')).first()

