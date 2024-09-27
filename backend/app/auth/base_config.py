from fastapi.security import OAuth2PasswordBearer
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from backend.app.auth.manager import get_user_manager
from backend.app.auth.models import User

# router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

cookie_transport = CookieTransport(cookie_name='sweet', cookie_max_age=3600)
SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


# @router.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}
#

# @router.post("/users", response_model=UserSchema)
# async def register_user(
#         user: UserCreateSchema,  session: Session = Depends(get_session)
# ):
#     """Registration of new user"""
#     try:
#         return create_user(session, user)
#     except IntegrityError:
#         raise HTTPException(status_code=422, detail='User already exists')
#
#
# @router.get("/users/{user_id}")  # получение user по id от базы данных
# def get_user(session: Session = Depends(get_session)):
#     yield SQLAlchemy
#     # user = session.query(User).filter(User.id == user_id).first()
#     # if user is None:
#     #     raise HTTPException(status_code=404, detail="User not found")
#     # return user



