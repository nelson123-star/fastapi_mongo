from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document, Link

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[List[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email":"fastapi@main.com",
                "username":"strong",
                "events":[]
            }
        }

class UserSignIn (BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email":"fastapi@main.com",
                "password":"strong",
                "events":[]
            }
        }