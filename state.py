from typing import TypedDict


class TravelState(TypedDict):
    destination: str
    duration: int
    budget: str
    interests: str

    research: str
    itinerary: str
    guide: str