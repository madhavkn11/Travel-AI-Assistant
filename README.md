# 🌍 TravelAI Assistant

An AI-powered travel planning assistant that generates personalized travel itineraries, recommends hotels and restaurants, displays real-time weather, interactive maps, flight information, and helps users plan complete trips using Generative AI.

---

## 📖 About the Project

TravelAI Assistant is an intelligent travel planning application built using **Streamlit**, **LangGraph**, and **Groq LLM**. The application combines AI-generated travel recommendations with real-time travel information to create personalized travel guides tailored to each user's destination, budget, duration, and interests.

Whether you're planning a weekend getaway or a week-long vacation, TravelAI Assistant provides everything from itinerary planning to hotel recommendations in one place.

---

## ✨ Key Features

### 🤖 AI-Powered Travel Guide
- Generates personalized travel guides using Groq LLM.
- Provides recommendations based on:
  - Destination
  - Budget
  - Duration
  - Travel interests

---

### 📅 Smart Itinerary Generation
Creates a complete day-wise itinerary including:
- 🌅 Morning activities
- ☀ Afternoon activities
- 🌇 Evening activities
- Restaurant suggestions
- Transportation recommendations

---

### 🌍 Interactive Maps
- Displays the selected destination on an interactive map.
- Helps users explore nearby attractions visually.

---

### 🌦 Live Weather Information
Shows current weather including:
- Temperature
- Weather condition
- Humidity
- Wind speed

---

### 🏨 Hotel Recommendations
Provides:
- Recommended hotels
- Ratings
- Price information (if available)
- Booking links

---

### 🍽 Restaurant Recommendations
Displays:
- Popular restaurants
- Ratings
- Location
- Description
- Direct links

---

### ✈ Flight Information
- Displays flight information from major Indian cities.
- Shows estimated/live fares *(depending on API integration)*.
- Includes quick booking links for:
  - MakeMyTrip
  - Goibibo
  - Cleartrip
  - IndiGo
  - Air India

---

### 📍 Google Maps Integration
Open the destination directly in Google Maps with a single click.

---

### 💬 AI Travel Chat Assistant
Chat with the AI to:
- Ask travel-related questions
- Get additional recommendations
- Receive destination-specific suggestions

---

### 📄 Markdown Export
Download the generated travel guide in Markdown format for future reference.

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### AI & LLM
- Groq
- LangChain
- LangGraph

### APIs & Services
- Weather API
- Google Maps
- Folium
- OpenStreetMap
- Travel Search API
- SerpApi (Google Flights) *(optional/in progress)*

### Libraries
- Pandas
- Requests
- python-dotenv
- streamlit-folium

---

## 📂 Project Structure

```
TravelAI_Assistant/
│
├── app.py
├── workflow.py
├── agents.py
├── prompts.py
├── config.py
├── state.py
├── utils.py
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
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/madhavkn11/Travel-AI-Assistant.git

cd Travel-AI-Assistant
```

---

### 2️⃣ Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

WEATHER_API_KEY=YOUR_WEATHER_API_KEY

SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

```
User Inputs
      │
      ▼
Destination + Budget + Duration + Interests
      │
      ▼
Travel Research Agent
      │
      ▼
AI Research Report
      │
      ▼
Itinerary Planner
      │
      ▼
Travel Guide Generator
      │
      ▼
Fetch Weather
      │
      ▼
Fetch Hotels
      │
      ▼
Fetch Restaurants
      │
      ▼
Generate Interactive Map
      │
      ▼
Display Results in Streamlit
```

---

---

## 🎯 Future Enhancements

- Live Google Flights Integration
- Dynamic Airport Detection
- Hotel Price Comparison
- Multi-language Support
- User Authentication
- Save Trip History
- Currency Converter
- Email Travel Guide
- PDF Export
- Nearby Attractions using GPS
- Offline Travel Guide

---

## 📈 Skills Demonstrated

- Generative AI
- Prompt Engineering
- LangGraph Workflows
- LangChain
- API Integration
- Python Development
- Streamlit Application Development
- REST APIs
- Data Processing
- Interactive UI Development

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 👨‍💻 Author

**Madhav Karthik Nambi**

- GitHub: https://github.com/madhavkn11
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

**Built with ❤️ using Python, Streamlit, LangGraph, LangChain and Generative AI.**
