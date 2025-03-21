from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings
from fastapi.responses import RedirectResponse

import uvicorn

app = FastAPI()

settings = Settings()

#Register routes
app.include_router(user_router, prefix = "/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.31.182", port=8080, reload=True)