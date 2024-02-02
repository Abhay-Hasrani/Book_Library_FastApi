from sqlalchemy import Column, DateTime, Integer, String, func
from models import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(255),unique=True,index=True)
    username = Column(String(30))
    hashed_password = Column(String(256))
    role = Column(String(20))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    books = relationship("Book", secondary="user_book", back_populates="users")