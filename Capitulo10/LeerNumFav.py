from pathlib import Path
import json

path = 'textos/numFav.json'
ruta = Path(path)

print('Leer Numero Favorito')
print('------------------------')

if ruta.exists():
    contenido = ruta.read_text()
    numero = json.loads(contenido)
    print(f'¡Se cual es tu número favorito! Es el {numero}')
else:
    print('No existe el fichero')