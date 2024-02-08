from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from app import models
from app.controllers.auth_controller import get_current_user
from app.db.database import engine
from app.helpers.env_helper import get_env_variable
from app.routers import auth, books, requests, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    get_env_variable("FRONTEND_BASE_URL")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def redirect():
    return RedirectResponse(url="/books")

app.include_router(auth.router, prefix="/auth", tags=['Auth'])
app.include_router(users.router, prefix="/users", tags=['User'])
app.include_router(books.router, dependencies=[Depends(get_current_user)], prefix="/books", tags=['Book'])
app.include_router(requests.router, dependencies=[Depends(get_current_user)], prefix="/requests", tags=['Book-Request'])
