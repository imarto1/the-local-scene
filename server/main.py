from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

from models.event import Event

app = FastAPI()


@app.get("/")
def seal():
    return FileResponse(path="./horse.png")


@app.post("/event")
def create_event(event: Event):
    """
    publishes a new event to the system.
    """
    return event.title
