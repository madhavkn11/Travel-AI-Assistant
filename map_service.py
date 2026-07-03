from geopy.geocoders import Nominatim
import folium


class MapService:

    def __init__(self):
        self.geolocator = Nominatim(user_agent="travel_ai")

    def create_map(self, destination):

        location = self.geolocator.geocode(destination)

        if not location:
            return None

        travel_map = folium.Map(
            location=[location.latitude, location.longitude],
            zoom_start=12
        )

        folium.Marker(
            [location.latitude, location.longitude],
            popup=destination,
            tooltip=destination
        ).add_to(travel_map)

        return travel_map