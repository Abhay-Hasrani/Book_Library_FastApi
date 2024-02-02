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
