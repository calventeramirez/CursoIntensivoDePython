def ciudad_pais(ciudad, pais):
    return f'{ciudad.title()}, {pais.title()}'

ciudad = ciudad_pais('Málaga', 'España')
print(ciudad)
ciudad = ciudad_pais('Londres', 'Reino Unido')
print(ciudad)
ciudad = ciudad_pais('Washington DC', 'EEUU')
print(ciudad)