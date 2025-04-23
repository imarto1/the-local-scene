import os

from elasticsearch import Elasticsearch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.event import Event, GetEventsBody, GetEventsResponse

client = Elasticsearch(
    hosts=["https://localhost:32768/"],
    api_key=os.getenv("ELASTIC_API_KEY", "ZVJJRldKWUJHbi1mVG5feHlMWks6blFfdzBKYUZSYWdwSjVTelRnN2QxQQ"),
    verify_certs=False,
)
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def fetch_events(lon, lat, distance):
    return client.search(
        index="events",
        query={
            "bool": {
                "filter": {
                    "geo_distance": {
                        "distance": f"{distance}km",
                        "location": {
                            "lon": lon,
                            "lat": lat
                        }
                    }
                }
            }
        }
    )["hits"]["hits"]


@app.get("/events", response_model=GetEventsResponse)
def get_events(lon: float, lat: float, radius: int):
    events = fetch_events(lon, lat, radius)
    return GetEventsResponse(events=[{"id": event["_id"], **event["_source"]} for event in events])


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
