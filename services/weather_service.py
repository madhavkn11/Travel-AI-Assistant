import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")

    def get_weather(self, destination):

        try:

            url = (
                f"http://api.weatherapi.com/v1/current.json"
                f"?key={self.api_key}&q={destination}"
            )

            response = requests.get(url, timeout=10)

            data = response.json()

            if "current" not in data:
                print("Weather API Error:", data)
                return None

            return {
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind": data["current"]["wind_kph"]
            }

        except Exception as e:
            print("Weather Error:", e)
            return None