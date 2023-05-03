import pandas as pd
import brazilcep as bc
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from brazilcep import get_address_from_cep, WebService
from brazilcep import get_address_from_cep

def get_address(cep):
    endereco = bc.get_address_from_cep(cep, webservice=WebService.VIACEP)
    return endereco['street'] + ", " + endereco['district'] + ", " + endereco['city'] + " - " + endereco['uf']

# DataFrame de teste

df= pd.read_csv('bulk2.csv', converters={'cep_str': str})

#Troque test_app pelo nome da sua aplicação/sistema
geolocator = Nominatim(user_agent="test_app")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)

# Cria a coluna address com os endereços retornados a partir do CEP
df['address'] = df['cep_str'].apply(get_address)

# Cria a coluna location com o local retornado a partir do endereço
df['location'] = df['address'].apply(geocode)

# Seleciona a latitude e longitude que está dentro do local
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
print(df)










