from models.user_book import UserBook
from models.book import Book


def json_book(book: Book):
    id = str(book.id)
    imageUrl = str(book.imageUrl)
    title = str(book.title)
    description = str(book.description)
    author = str(book.author)
    launched = str(book.launched)
    rating = str(book.rating)
    created_at = str(book.created_at)
    updated_at = str(book.updated_at)
    return {"id":id,"imageUrl":imageUrl,"title":title,"description":description,"author":author,"launched":launched,"rating":rating,"created_at":created_at,"updated_at":updated_at}

def json_book_request(user_book: UserBook):
    user_id = str(user_book.user_id)
    book_id = str(user_book.book_id)
    status = str(user_book.status)
    created_at = str(user_book.created_at)
    updated_at = str(user_book.updated_at)
    return {"user_id":user_id,"book_id":book_id,"status":status,"created_at":created_at,"updated_at":updated_at}