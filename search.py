import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


class SearchService:

    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def search(self, query):

        try:

            result = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=3
            )

            return result.get("results", [])

        except requests.exceptions.ConnectionError:
            print("Tavily connection failed.")
            return []

        except requests.exceptions.Timeout:
            print("Tavily timed out.")
            return []

        except Exception as e:
            print("Search Error:", e)
            return []