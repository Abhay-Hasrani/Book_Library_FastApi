from fastapi import Depends, FastAPI
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
from controllers.auth_controller import get_current_user
from db.database import engine
import models
from routers import auth, books, users

#load .env variables at before creating instance
load_dotenv()

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def redirect():
    return RedirectResponse(url="/books")

app.include_router(auth.router, prefix="/auth", tags=['Auth-Routes'])
app.include_router(users.router, prefix="/users", tags=['User-Routes'])
app.include_router(books.router, dependencies=[Depends(get_current_user)], prefix="/books", tags=['Book-Routes'])
