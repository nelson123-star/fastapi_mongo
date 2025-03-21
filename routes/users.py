from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from database.connection import Database

user_router = APIRouter(
    tags=["User"]
)

user_database = Database(User)

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with supplied username exists"
        )
    await user_database.save(user)
    return {
        "message": "User successfully registered!"
    }

@user_router.post("/signin")
async def sign_user_in(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with supplied username exists"
        )
    await user_database.save(user)
    return {
        "message": "User successfully registered!"
    }