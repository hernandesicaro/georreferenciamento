import pandas as pd
import numpy as np

#Vou usar o pacote do python de ceps do Brasil
#antes era conhecido como pycep_correios
#mas atualmente é o brazilcep (instalar com pip + import)

import brazilcep as bc

#além do pacote do cep eu tenho que importar
#o pacote de georreferenciamento mais usado do python
#que é o GeoPy (instarlar com pip + import)

from geopy.geocoders import Nominatim

#'from': An alternate form of the import statement allows individual
# objects from the module to be imported directly into the caller’s
# symbol table.

address = bc.get_address_from_cep('87303253')

geolocator = Nominatim(user_agent="test_teste")
location=geolocator.geocode(address)
print(address)
print("\n")
print(location)
print("\n")
print(location.latitude, location.longitude)






