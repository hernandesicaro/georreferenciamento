import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter




geolocator = Nominatim(user_agent="tese_teste")

df = pd.DataFrame({'address': ['Rua Escobar Ortiz Vila Nova Conceição São Paulo',
                               'Rua Emílio Berla Copacabana Rio de Janeiro',
                               'Rua Madagascar Parque Oratorio Santo André']})

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df['location'] = df['address'].apply(geocode)

df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

print(df)