from typing import List
from beanie import PydanticObjectId
from sqlalchemy.event import Events

from database.connection import  get_session
from fastapi import APIRouter, HTTPException, status, Depends
from models.events import Event, EventUpdate
from sqlmodel import select

event_router = APIRouter(
    tags=["Events"]
)

# event_database = Database(Event)

@event_router.post("/new")
async def create_event(new_event: Event,
session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
    "message": "Event created successfully"
    }

@event_router.get("/", response_model=List[Event])
async def rereieve_all_events(session=Depends(get_session))->List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id:int, session = Depends(get_session))->Event:
    event = session.get(Events, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.delete("/delete/{id}")
async def delete_event(id: int, session = Depends(get_session)) -> dict:
    event = session.get(Events, id)
    if event:
        session.delete(event)
        session.commit()

        return {
            "message":"Event deleted successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )




