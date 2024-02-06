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