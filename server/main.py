from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from models.event import Event

app = FastAPI()


@app.get("/")
def seal():
    return "an morte, irmicus!"


@app.post("/event")
def create_event(event: Event):
    """
    publishes a new event to the system.
    """
    return event.title
