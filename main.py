from datetime import date
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models.user import User
from models.book import Book
from models.user_book import UserBook
from db.database import SessionLocal, engine
import models

#load .env variables at before creating instance
load_dotenv()

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/")
async def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    books = db.query(Book).all()
    userbooks = db.query(UserBook).all()
    return [users,books,userbooks]

@app.get("/user")
async def get_users(): 
    db = SessionLocal()
    # new_user = User(email='example@example.com', username='example_user', hashed_password='hashed_password', role='user')
    # db.add(new_user)
    new_book = Book(
    imageUrl="http://example.com/book.jpg",
    title="Sample Book",
    description="This is a sample book description.",
    author="Sample Author",
    launched=date(2022, 1, 1),
    rating=5
    )
    db.add(new_book)
    db.commit()
    return {}
