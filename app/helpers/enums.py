from sqlalchemy import Enum

class UserRole(str, Enum):
    ADMIN = 'Admin'
    STUDENT = 'Student'

class BookRequestStatus(str ,Enum):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    RETURNED = 'Returned'