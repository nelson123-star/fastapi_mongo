from sqlmodel import SQLModel, Session, create_engine
from models.events import Event
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings
from models.users import User
from models.events import Event

async def initialize_database (self):
    client = AsyncIOMotorClient(self.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Event, User]
    )


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[]
        )

        class Config:
            env_file = ".env"

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread":False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session


