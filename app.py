import streamlit as st
from streamlit_folium import st_folium
from workflow import travel_graph
from styles import load_css
from utils import save_markdown

from services.weather_service import WeatherService
from services.travel_service import TravelService
from services.flight_service import FlightService
from services.chat_service import ChatService
from map_service import MapService


st.set_page_config(
    page_title="TravelAI Assistant",
    page_icon="🌍",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)


# ===========================
# Session State
# ===========================

defaults = {
    "guide": None,
    
    "image_url": None,
    "weather": None,
    "hotels": [],
    "restaurants": [],
    "flight_info": None,
    "maps_link": "",
    "destination": "",
    "duration": 5,
    "budget": "",
    "interests": [],
    "messages": [],
    "chat_service": ChatService()
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ===========================
# Header
# ===========================

st.markdown(
    """
<div style="
background:linear-gradient(135deg,#2563eb,#1d4ed8);
padding:30px;
border-radius:18px;
margin-bottom:20px;
color:white;
">

<h1 style="margin:0;">
🌍 TravelAI Assistant
</h1>

<p style="font-size:18px;margin-top:10px;">
Your AI-powered travel companion for personalized itineraries,
live weather, hotels, restaurants, maps and AI travel planning.
</p>

</div>
""",
    unsafe_allow_html=True
)


st.markdown(
    """
<div style="
background:linear-gradient(90deg,#2563eb,#1d4ed8);
padding:20px;
border-radius:15px;
margin-bottom:20px;
color:white;
">

<h2>
Plan Smarter. Travel Better.
</h2>

<p>
Generate complete AI-powered travel itineraries with live weather,
interactive maps, nearby hotels and restaurants.
</p>

</div>
""",
    unsafe_allow_html=True
)


# ===========================
# Sidebar
# ===========================

with st.sidebar:

    st.header("✈ Trip Planner")

    destination = st.text_input(
        "Destination",
        value=st.session_state.destination
    )

    duration = st.number_input(
        "Duration (Days)",
        min_value=1,
        max_value=30,
        value=st.session_state.duration
    )

    budget = st.number_input(
    "💰 Budget (₹)",
    min_value=0,
    step=1000,
    value=50000
)
    interests = st.multiselect(
    "Interests",
    [
        "Adventure",
        "Nature",
        "Beaches",
        "Temples",
        "Shopping",
        "Food",
        "Culture",
        "Historical Places",
        "Nightlife",
        "Photography",
        "Wildlife"
    ],
    default=st.session_state.interests
)

    st.divider()

    st.subheader("✨ Features")

    st.success("✔ AI Itinerary")
    st.success("✔ Live Weather")
    st.success("✔ Hotels")
    st.success("✔ Restaurants")
    st.success("✔ Maps")
    st.success("✔ Flight Information")
    st.success("✔ AI Chat")
    

    st.divider()

    st.caption("Powered by")
    st.write("• LangGraph")
    st.write("• Groq")
    st.write("• Tavily")
    st.write("• Streamlit")

    st.divider()

    generate = st.button(
        "🚀 Generate Travel Guide",
        use_container_width=True
    )


# ===========================
# Generate Guide
# ===========================

if generate:

    if destination.strip() == "":
        st.error("Please enter a destination.")

    else:

        state = {
            "destination": destination,
            "duration": duration,
            "budget": budget,
            "interests": ", ".join(interests),
            "research": "",
            "itinerary": "",
            "guide": ""
        }

        progress = st.progress(0)

        progress.progress(
            15,
            text="Researching destination..."
        )

        result = travel_graph.invoke(state)

        progress.progress(
            55,
            text="Generating itinerary..."
        )

        guide = result["guide"]

        save_markdown(guide)

        

        
        weather_service = WeatherService()
        travel_service = TravelService()
        flight_service = FlightService()

        
        weather = weather_service.get_weather(destination)
        hotels = travel_service.get_hotels(destination)
        restaurants = travel_service.get_restaurants(destination)
        maps_link = travel_service.get_maps_link(destination)
        flight_info = flight_service.get_flight_info(destination)

        st.session_state.guide = guide
        
        
        st.session_state.weather = weather
        st.session_state.hotels = hotels
        st.session_state.restaurants = restaurants
        st.session_state.maps_link = maps_link
        st.session_state.flight_info = flight_info
        st.session_state.destination = destination
        st.session_state.duration = duration
        st.session_state.budget = budget
        st.session_state.interests = interests
        st.session_state.messages = []

        progress.progress(
            100,
            text="Travel Guide Ready!"
        )

        progress.empty()

        st.success("Travel Guide Generated Successfully!")
    # ===========================
# Display Results
# ===========================
st.markdown("""
<h1 style='text-align:center;color:#2563EB;'>
🌍 TravelAI Assistant
</h1>
<h4 style='text-align:center;color:gray;'>
Plan your perfect trip with AI-powered travel planning
</h4>
""", unsafe_allow_html=True)
if st.session_state.guide:

    

    

    # ===========================
    # Interactive Map
    # ===========================
    

   
    

    st.subheader("🗺 Interactive Map")

    map_service = MapService()

    travel_map = map_service.create_map(
        st.session_state.destination
    )

    if travel_map:

        st_folium(
            travel_map,
            width=1000,
            height=500
        )

    else:

        st.info("Map unavailable.")

    # ===========================
    # Weather
    # ===========================

    st.divider()

    st.subheader("🌦 Current Weather")

    weather = st.session_state.weather
    
    if weather:
     with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']}°C"
            )

        with c2:
            st.metric(
                "☁ Condition",
                weather["condition"]
            )

        with c3:
            st.metric(
                "💧 Humidity",
                f"{weather['humidity']}%"
            )

        with c4:
            st.metric(
                "💨 Wind",
                f"{weather['wind']} km/h"
            )

    else:

        st.warning(
            "Weather information unavailable."
        )

    # ===========================
    # Flight Information
    # ===========================

    st.divider()
    

    
    import pandas as pd

    st.subheader("✈ Estimated Flight Fares (Economy • One-way)")

    flight_data = pd.DataFrame({
    "From": [
        "Hyderabad",
        "Mumbai",
        "Delhi",
        "Kolkata",
        "Bengaluru"
    ],
    "To": [
        st.session_state.destination,
        st.session_state.destination,
        st.session_state.destination,
        st.session_state.destination,
        st.session_state.destination
    ],
    "Approx. Lowest Fare": [
        "₹2,800",
        "₹3,900",
        "₹5,200",
        "₹4,100",
        "₹2,500"
    ]
})

    st.dataframe(
    flight_data,
    use_container_width=True,
    hide_index=True
)
    st.caption(
    "Estimated economy one-way fares from major Indian cities. "
    "Actual fares may vary based on season, airline and booking date."
)
    # ===========================
    # Flight Booking
    # ===========================
    st.divider()
    st.markdown("### ✈ Book Flights")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.link_button(
            "MakeMyTrip",
            "https://www.makemytrip.com/flights/",
            use_container_width=True
        )

    with col2:

        st.link_button(
            "Goibibo",
            "https://www.goibibo.com/flights/",
            use_container_width=True
        )

    with col3:

        st.link_button(
            "Cleartrip",
            "https://www.cleartrip.com/flights",
            use_container_width=True
        )

    col4, col5 = st.columns(2)
    

    with col4:

        st.link_button(
            "IndiGo",
            "https://www.goindigo.in/",
            use_container_width=True
        )

    with col5:

        st.link_button(
            "Air India",
            "https://www.airindia.com/",
            use_container_width=True
        )

    # ===========================
    # Recommended Restaurants
    # ===========================

    st.divider()
    st.subheader("🍽 Recommended Restaurants")
    if st.session_state.restaurants:

        for restaurant in st.session_state.restaurants:

            with st.container(border=True):

                st.markdown(
                    f"### 🍽 {restaurant.get('title', 'Restaurant')}"
                )

                if restaurant.get("snippet"):
                    st.write(restaurant["snippet"])

                if restaurant.get("rating"):
                    st.write(f"⭐ Rating: {restaurant['rating']}")

                if restaurant.get("address"):
                    st.write(f"📍 {restaurant['address']}")

                if restaurant.get("url"):

                    st.link_button(
                        "View Restaurant",
                        restaurant["url"],
                        use_container_width=True
                    )

    else:

        st.info("No restaurant recommendations available.")

    # ===========================
    # Recommended Hotels
    # ===========================

    st.divider()
    st.subheader("🏨 Recommended Hotels")

    if st.session_state.hotels:

        for hotel in st.session_state.hotels:

            with st.container(border=True):

                st.markdown(
                    f"### 🏨 {hotel.get('title', 'Hotel')}"
                )

                if hotel.get("snippet"):
                    st.write(hotel["snippet"])

                if hotel.get("rating"):
                    st.write(f"⭐ Rating: {hotel['rating']}")

                if hotel.get("price"):
                    st.write(f"💰 {hotel['price']}")

                if hotel.get("address"):
                    st.write(f"📍 {hotel['address']}")

                if hotel.get("url"):

                    st.link_button(
                        "Book Hotel",
                        hotel["url"],
                        use_container_width=True
                    )

    else:

        st.info("No hotel recommendations available.")

    # ===========================
    # Google Maps
    # ===========================

    st.divider()
    st.subheader("📍 Explore on Google Maps")

    if st.session_state.maps_link:
       with st.container(border=True):
        st.link_button(
            "Open in Google Maps",
            st.session_state.maps_link,
            use_container_width=True
        )

    else:

        st.info("Google Maps link unavailable.")

    # ===========================
    # Trip Summary
    # ===========================

    st.divider()
    st.subheader("📊 Trip Summary")
    with st.container(border=True):
     col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📅 Duration",
            f"{st.session_state.duration} Days"
        )

    with col2:

        st.metric(
            "💰 Budget",
            st.session_state.budget
        )

    with col3:

        st.metric(
            "❤️ Interests",
            len(st.session_state.interests)
        )

        if st.session_state.interests:

            st.caption(
                ", ".join(st.session_state.interests)
            )

        else:

            st.caption("No interests selected.")
    
        # ===========================
    # Travel Guide & Downloads
    # ===========================

    st.divider()

    guide_tab, download_tab = st.tabs(
        [
            "📖 Travel Guide",
            "📥 Download"
        ]
    )

    # ===========================
    # Travel Guide
    # ===========================

    with guide_tab:

        st.markdown(st.session_state.guide)

    # ===========================
    # Downloads
    # ===========================

    with download_tab:

        st.subheader("Download Your Travel Guide")

        try:

                with open(
                    "outputs/travel_guide.md",
                    "r",
                    encoding="utf-8"
                ) as md_file:

                    st.download_button(
                        label="📝 Download Markdown",
                        data=md_file.read(),
                        file_name="travel_guide.md",
                        mime="text/markdown",
                        use_container_width=True
                    )

        except FileNotFoundError:

                st.warning("Markdown file not found.")

    # ===========================
    # AI Travel Chat
    # ===========================

    st.divider()

    st.subheader("🤖 TravelAI Chat")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask anything about your trip..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner(
                "TravelAI is thinking..."
            ):

                answer = st.session_state.chat_service.chat(
                    st.session_state.guide,
                    prompt
                )

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

else:

    st.info(
        "👈 Enter your destination and click **Generate Travel Guide** to begin."
    )


# ===========================
# Footer
# ===========================

st.divider()

st.markdown(
    """
<div style="text-align:center;color:#6b7280;font-size:14px;">
<b>TravelAI Assistant</b><br>
Built using Streamlit • LangGraph • Groq • Tavily
</div>
""",
    unsafe_allow_html=True
)

