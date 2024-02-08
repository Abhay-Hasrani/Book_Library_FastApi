import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.models.user import User
from starlette import status
from jose import jwt, JWTError
from app.controllers.users_controller import bcrypt_context

load_dotenv()

ALGORITHM = os.environ.get("ALGORITHM") 
SECRET_KEY = os.environ.get("SECRET_KEY")  


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user
    

def create_access_token(username: str, user_id: int, role: str):
    encode = {'username': username, 'id': user_id, 'role': role}
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)



def login_for_access_token(db: Session, form_data: dict):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
        
    token = create_access_token(user.username, user.id, user.role)
    return {'access_token': token, 'token_type': 'bearer'}

        

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
        id: int = payload.get('id')
        role: str = payload.get('role')
        if username is None or id is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Could not validate user.')
        return {'username': username, 'id': id, 'role': role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')