🌍 TravelAI Assistant

An AI-powered travel planning assistant that generates personalized travel itineraries, recommends hotels and restaurants, provides real-time weather information, displays interactive maps, and helps users plan their trips efficiently using Large Language Models (LLMs).

📌 Overview

TravelAI Assistant is an intelligent travel planner built using Streamlit, LangGraph, and Groq LLM. It creates customized travel guides based on the user's destination, trip duration, budget, and interests while integrating real-time travel information such as weather, maps, hotels, restaurants, and flight details.

✨ Features
🤖 AI-Powered Travel Planning
Generates personalized travel guides using Groq LLM.
Creates customized itineraries based on:
Destination
Duration
Budget
User interests
📅 Day-wise Itinerary Generation
Automatically plans each day of the trip.
Includes:
Morning activities
Afternoon activities
Evening activities
Balances sightseeing, dining, and relaxation.
🌍 Interactive Destination Map
Displays an interactive map of the selected destination.
Helps users visualize the location before traveling.
🌦 Real-Time Weather Information

Shows:

Temperature
Weather conditions
Humidity
Wind speed
🏨 Hotel Recommendations

Suggests hotels with:

Hotel name
Description
Ratings (if available)
Pricing (if available)
Booking links
🍽 Restaurant Recommendations

Provides:

Popular restaurants
Ratings
Location
Description
Direct links
✈ Flight Information
Displays estimated or live flight fares (based on integration).
Supports flights from major Indian cities.
Flight booking shortcuts for:
MakeMyTrip
Goibibo
Cleartrip
IndiGo
Air India
📍 Google Maps Integration
Open the destination directly in Google Maps.
💬 AI Travel Assistant
Chat with the AI for travel-related questions.
Ask follow-up questions about the destination.
📄 Markdown Export
Download the generated travel guide as a Markdown file.
🎨 Modern UI
Responsive Streamlit interface
Interactive metrics
Tables
Maps
Cards
External travel links
🛠 Tech Stack
Frontend
Streamlit
HTML
CSS
Backend
Python
AI & LLM
Groq
LangChain
LangGraph
APIs & Services
Weather API
Google Maps
Folium
OpenStreetMap
Search API
SerpApi (Google Flights) (optional/in progress)
Libraries
Pandas
Requests
python-dotenv
streamlit-folium
📂 Project Structure
TravelAI_Assistant/
│
├── app.py
├── workflow.py
├── agents.py
├── prompts.py
├── config.py
├── utils.py
├── state.py
│
├── services/
│   ├── weather_service.py
│   ├── travel_service.py
│   ├── flight_service.py
│   ├── chat_service.py
│   └── image_service.py
│
├── ui/
│   ├── sidebar.py
│   ├── downloads.py
│   ├── results.py
│   ├── metric.py
│   └── header.py
│
├── assets/
├── outputs/
├── requirements.txt
└── README.md
🚀 Installation
1. Clone the Repository
git clone https://github.com/madhavkn11/Travel-AI-Assistant.git
cd Travel-AI-Assistant
2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Create a .env File
GROQ_API_KEY=YOUR_GROQ_API_KEY
WEATHER_API_KEY=YOUR_WEATHER_API_KEY
SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
5. Run the Application
streamlit run app.py
🖥 Usage
Enter your destination.
Choose trip duration.
Select your budget.
Choose your interests.
Click Generate Travel Guide.
Explore:
AI-generated itinerary
Weather
Hotels
Restaurants
Interactive map
Flight information
Download the travel guide.
