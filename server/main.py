from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from models.event import Event

app = FastAPI()


@app.get("/")
def seal():
    return HTMLResponse(f"""
    <img src='seal-spinning-around.gif'/>
    """)

@app.post("/event")
def create_event(event: Event):
    """
    publishes a new event to the system.
    """
    return event.title
