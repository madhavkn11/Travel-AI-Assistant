from pydantic import BaseModel
from typing import List


class DayPlan(BaseModel):
    day: int
    morning: str
    afternoon: str
    evening: str
    estimated_cost: str


class TravelGuide(BaseModel):

    destination_overview: str

    attractions: List[str]

    hotels: List[str]

    restaurants: List[str]

    transportation: List[str]

    itinerary: List[DayPlan]

    budget_summary: str

    packing_checklist: List[str]

    travel_tips: List[str]