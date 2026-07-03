from search import SearchService
from config import llm


class FlightService:

    def __init__(self):
        self.search = SearchService()

    def get_flight_info(self, destination):

        query = f"""
Flights from major Indian cities to {destination}.

Find:

- Average airfare in INR
- Cheapest months to fly
- Best time to book
- Major airlines
- Nearest airport
- Airport code

Use information from:

MakeMyTrip
Goibibo
Cleartrip
EaseMyTrip
Skyscanner India
IndiGo
Air India
"""

        results = self.search.search(query)

        context = ""

        for item in results:

            context += f"""
Title: {item.get('title', '')}

Content:
{item.get('content', '')}

Source:
{item.get('url', '')}

-------------------------
"""

        prompt = f"""
You are an AI travel assistant.

Using the search results below, generate a concise flight summary.

Return exactly in this format:

✈ Nearest Airport

🛫 Airport Code

🛩 Major Airlines

💰 Approximate Fare (INR)

📅 Best Time to Book

✈ Travel Tip

If exact airfare is unavailable,
provide a realistic estimated range
based on typical domestic flights in India.

If the booking window is unavailable,
recommend the common travel practice
(2–6 weeks before departure).

Clearly indicate when an estimate is used.

Search Results:

{context}
"""

        response = llm.invoke(prompt)

        return response.content