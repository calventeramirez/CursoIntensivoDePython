from pathlib import Path
import json

path = 'textos/numFav.json'
ruta = Path(path)

print('Guardar Numero Favorito')
print('------------------------')

fav = int(input('Introduzca su numero favorito: '))
contenido = json.dumps(fav) #preparo el numero para enviar al archivo

ruta.write_text(contenido) #escribo el texto en el fichero

print('Numero guardado correctamente')