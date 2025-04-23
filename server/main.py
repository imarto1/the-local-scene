from fastapi import FastAPI

from models.event import Event, GetEventsBody, GetEventsResponse
import os
from elasticsearch import Elasticsearch


client = Elasticsearch(
    hosts=["https://localhost:32771"],
    api_key=os.getenv("ELASTIC_API_KEY", "ZVJJRldKWUJHbi1mVG5feHlMWks6blFfdzBKYUZSYWdwSjVTelRnN2QxQQ"),
    verify_certs=False,
)
app = FastAPI()


@app.get("/events", response_model=GetEventsResponse)
def get_events(body: GetEventsBody):
    return GetEventsResponse(events=[])


@app.post("/event")
def create_event(event: Event):
    """
    publishes a new event to the system.
    """
    resp = client.index(
        index="events",
        document=event.model_dump(mode="json")
    )
    return resp
