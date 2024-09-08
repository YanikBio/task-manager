from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get("/")
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(operation)
    await session.execute(query)
    return
