from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import conn

import uvicorn

app = FastAPI()

#Register routes

app.include_router(user_router, prefix = "/user")
app.include_router(event_router, prefix="/event")

@app.on_event("startup")
def on_startup():
    conn()

# if __name__ == "main":
#     uvicorn.run("main:app", host="192.168.31.182", port = 8080, reload = True)