from typing import Optional, Tuple, Literal

from pydantic import BaseModel, Field

EVENT_TYPE = Literal["announcement", "request", "warning"]


class Event(BaseModel):
    title: str = Field(description="The title of the event.")
    description: Optional[str] = Field(description="The full description of the event.")
    type: EVENT_TYPE = Field(description="The type of the event, e.g announcement, request ect.")
    icon: str = Field(description="The string the corresponds to an icon that will appear in the event.")
    location: Tuple[float, float] = Field(description="The location the event occurs in. (in long and lat)")
    radius: Optional[int] = Field(
        description="A radius around the event in which the event is occurring, (if applicable)."
    )
