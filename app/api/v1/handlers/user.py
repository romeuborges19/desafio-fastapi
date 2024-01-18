from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@user_router.post('/create')
async def create_user():
    # user = 
    ...
