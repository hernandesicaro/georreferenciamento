import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

df = pd.read_csv("nom_test_bulk1.csv")

geolocator = Nominatim(user_agent="tese_teste")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df['point'] = (df['address'].apply(geocode)).apply(lambda loc: tuple(loc.point) if loc else None)

print(df)

#funcionou \o/
