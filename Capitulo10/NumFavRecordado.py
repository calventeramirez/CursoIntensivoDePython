from pathlib import Path
import json

path = 'textos/numFav.json'
ruta = Path(path)

def guardarNum():
    fav = int(input('Introduzca su numero favorito: '))
    contenido = json.dumps(fav)  # preparo el numero para enviar al archivo

    ruta.write_text(contenido)  # escribo el texto en el fichero

    print('Numero guardado correctamente')

def leerNum():
    if ruta.exists():
        contenido = ruta.read_text()
        numero = json.loads(contenido)
        print(f'¡Se cual es tu número favorito! Es el {numero}')
    else:
        print('No existe el fichero')

if ruta.exists():
    leerNum()
else:
    guardarNum()