# Diccionario con 3 rios y su ciudad, sacarlo en bucle como "El X discurre por Y"

rios = {
    'Amazonas': 'Brasil',
    'Misisipi': 'Minnesota',
    'Volga': 'Moscú',
}

for rio, pais in rios.items():
    print(f"El {rio} discurre por {pais}")