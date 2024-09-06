from typing import AsyncGenerator

from sqlalchemy import create_engine, Boolean, ForeignKey, Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session, Mapped, declared_attr, mapped_column

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends



DATABASE_URL = "sqlite+aiosqlite:///test.db"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session



# def get_session() -> Session:
#     '''получение доступа к данным базы данных'''
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

'''данные из базы данных можно получать через переменные моделей, кидая запросы базе данных'''

# def get_user(session: Session = Depends(get_session)) -> User:
#     yield SQLAlchemyUserDatabase(session, User)