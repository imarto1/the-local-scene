from fastapi import FastAPI

from models.event import Event

app = FastAPI()


@app.post("/event")
def create_event(event: Event):
    """
    publishes a new event to the system.
    """
    return event.title
    
