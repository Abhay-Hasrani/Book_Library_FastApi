from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
from db.database import engine
import models
from routers import books

#load .env variables at before creating instance
load_dotenv()

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def redirect():
    return RedirectResponse(url="/books")

app.include_router(books.router, prefix="/books", tags=['Book-Routes'])