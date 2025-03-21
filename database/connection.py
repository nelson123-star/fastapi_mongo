from typing import Optional
from beanie import init_beanie, PydanticObjectId
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    # DATABASE_URL: Optional[str] = "mongodb://127.0.0.1:27017/planner"
    DATABASE_URL: Optional[str] = None

    SECRET_KEY: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        document_models = [Event, User]
        await init_beanie(database=client.db_name, document_models=document_models)

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document):
        await document.create()
        return {"message":"СОБЫТИЕ СОЗДАНО"}

    async def get(self, id: PydanticObjectId):
        doc = await self.model.get(id)
        if doc: return doc
        return False

    async def get_all(self):
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel):
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}

        doc = await self.get(doc_id)
        if not doc: return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc: return False
        await doc.delete()
        return True

