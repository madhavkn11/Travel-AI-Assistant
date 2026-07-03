from search import SearchService
from config import llm
from prompts import (
    RESEARCH_PROMPT,
    ITINERARY_PROMPT,
    WRITER_PROMPT
)


class TravelResearchAgent:

    def __init__(self):
        self.search_service = SearchService()

    def run(self, destination, duration, budget, interests):

        search_results = self.search_service.search(
    f"""
    Travel guide for {destination}.

    Include:
    - Top attractions
    - Local culture
    - Food
    - Weather
    - Transportation
    - Budget tips
    - Best time to visit
    """
)

        search_text = ""

        for item in search_results:
            search_text += f"""
Title: {item.get('title','')}
Content: {item.get("content", "")[:200]}
"""

        prompt = RESEARCH_PROMPT.format(
            destination=destination,
            duration=duration,
            budget=budget,
            interests=interests,
            search_results=search_text
        )

        response = llm.invoke(prompt)

        return response.content


class ItineraryPlannerAgent:

    def run(self, research):

        prompt = ITINERARY_PROMPT.format(
            research=research
        )

        response = llm.invoke(prompt)

        return response.content


class TravelWriterAgent:

    def run(self, research, itinerary):

        prompt = WRITER_PROMPT.format(
            research=research,
            itinerary=itinerary
        )

        response = llm.invoke(prompt)

        return response.content

class FlightAgent:

    def run(self, flight_context):

        prompt = f"""
You are an expert travel assistant.

Using the flight search information below, generate a concise summary.

Return the information in exactly this format:

✈ Nearest Airport:
...

🛫 Airport Code:
...

🛩 Major Airlines:
• ...
• ...
• ...

💰 Approximate Flight Fare (from major Indian cities):
...

📅 Best Time to Book:
...

✈ Travel Tip:
...

Use only the information provided below.
If some information is unavailable, write "Not Available".

Flight Information:

{flight_context}
"""

        response = llm.invoke(prompt)

        return response.content 