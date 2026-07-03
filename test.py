from services.travel_service import TravelService

service = TravelService()

print("\nHotels:\n")
print(service.get_hotels("Bali"))

print("\nRestaurants:\n")
print(service.get_restaurants("Bali"))

print("\nAttractions:\n")
print(service.get_attractions("Bali"))

print("\nMaps:\n")
print(service.get_maps_link("Bali"))