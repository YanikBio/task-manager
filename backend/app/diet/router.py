from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session

router = APIRouter(
    prefix="/diet",
    tags=["Diet"]
)

