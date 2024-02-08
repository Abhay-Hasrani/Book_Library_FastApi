from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BookRequest(BaseModel):
    imageUrl: Optional[str]
    title: str
    description: str
    author: str
    launched: Optional[date]
    rating: int = Field(gt=0,lt=6)

class BookIssueRequest(BaseModel):
    book_id: int

class BookIssueStatusRequest(BaseModel):
    id: int
    book_id: int
    user_id: int
    status: str