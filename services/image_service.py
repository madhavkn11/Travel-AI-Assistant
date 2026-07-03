import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ImageService:

    def __init__(self):
        self.api_key = os.getenv("PEXELS_API_KEY")

    def get_image(self, destination):

        headers = {
            "Authorization": self.api_key
        }

        url = "https://api.pexels.com/v1/search"

        params = {
            "query": destination,
            "per_page": 1
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        data = response.json()

        if data.get("photos"):
            return data["photos"][0]["src"]["large"]

        return None