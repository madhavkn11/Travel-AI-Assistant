from search import SearchService


class TravelService:

    def __init__(self):
        self.search = SearchService()

    def get_hotels(self, destination):

        results = self.search.search(
            f"""
            Best hotels in {destination}.
            Prefer results from
            MakeMyTrip Hotels,
            Goibibo Hotels,
            Booking.com,
            Agoda,
            Cleartrip.
            """
        )

        trusted_sites = [
            "makemytrip.com",
            "goibibo.com",
            "booking.com",
            "agoda.com",
            "cleartrip.com"
        ]

        hotels = []

        for item in results:

            url = item.get("url", "").lower()

            if any(site in url for site in trusted_sites):

                hotels.append({
                    "title": item.get("title", ""),
                    "url": item.get("url", "")
                })

            if len(hotels) == 5:
                break

        return hotels

    def get_restaurants(self, destination):

        results = self.search.search(
            f"""
            Best restaurants in {destination}.
            Prefer results from
            Zomato,
            EazyDiner,
            Swiggy Dineout.
            """
        )

        trusted_sites = [
            "zomato.com",
            "eazydiner.com",
            "swiggy.com"
        ]

        restaurants = []

        for item in results:

            url = item.get("url", "").lower()

            if any(site in url for site in trusted_sites):

                restaurants.append({
                    "title": item.get("title", ""),
                    "url": item.get("url", "")
                })

            if len(restaurants) == 5:
                break

        return restaurants

    def get_attractions(self, destination):

        results = self.search.search(
            f"Top tourist attractions in {destination}"
        )

        attractions = []

        for item in results[:5]:

            attractions.append({
                "title": item.get("title", ""),
                "url": item.get("url", "")
            })

        return attractions

    def get_maps_link(self, destination):

        destination = destination.replace(" ", "+")

        return f"https://www.google.com/maps/search/{destination}"