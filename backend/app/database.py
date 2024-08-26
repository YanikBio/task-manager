from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)  # создание движжка базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # bind - присоединяем к движку


class Base(DeclarativeBase):
    """Base declarative class"""
    pass


def get_session():
    session = SessionLocal()  # мейкер, создающий сессионного менеджера
    try:
        yield session
    finally:
        session.close()