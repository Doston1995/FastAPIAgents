from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator 
from core.config import settings
from passlib.context import CryptContext

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()