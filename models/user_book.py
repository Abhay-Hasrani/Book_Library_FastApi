from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from models import Base


class UserBook(Base):
    __tablename__ = 'user_book'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    state = Column(String(20))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
