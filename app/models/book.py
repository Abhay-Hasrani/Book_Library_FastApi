from sqlalchemy import Column, Date, DateTime, Integer, String, func
from app.models import Base
from sqlalchemy.orm import relationship
from app.models.user_book import UserBook
from app.models.user import User

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True,index=True)
    imageUrl = Column(String(255))
    title = Column(String(length=255))
    description = Column(String(length=255))
    author = Column(String(length=100))
    launched = Column(Date)
    rating = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    users = relationship("User", secondary="user_book", back_populates="books")