from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_session
from ..schemas.auth import UserCreateSchema, UserSchema
from ..services.auth import create_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/users", response_model=UserSchema)
async def register_user(
        user: UserCreateSchema,  session: Session = Depends(get_session)
):
    """Registration of new user"""
    try:
        return create_user(session, user)
    except IntegrityError:
        raise HTTPException(status_code=422, detail='User already exists')