import pandas as pd
from geopy.geocoders import Nominatim




geolocator = Nominatim(user_agent="test_teste")


location=geolocator.geocode("Rua Tuim Moema São Paulo")


print(location)
print(location.latitude, location.longitude)