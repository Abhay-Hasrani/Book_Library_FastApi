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