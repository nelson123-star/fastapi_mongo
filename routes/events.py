from typing import List

from beanie import PydanticObjectId
from database.connection import get_session
from fastapi import APIRouter, HTTPException, status, Depends
from models.events import Event, EventUpdate

event_router = APIRouter(
    tags=["Events"]
)

@event_router.post("/new")
async def create_event(new_event: Event,
session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
    "message": "Event created successfully"
    }


