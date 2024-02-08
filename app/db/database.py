from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.helpers.env_helper import get_env_variable

MYSQL_HOST = get_env_variable("MYSQL_HOST")
MYSQL_USER = get_env_variable("MYSQL_USER")
MYSQL_PORT = get_env_variable("MYSQL_PORT")
MYSQL_PASSWORD = get_env_variable("MYSQL_PASSWORD")
MYSQL_DB_NAME = get_env_variable("MYSQL_DB_NAME")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)